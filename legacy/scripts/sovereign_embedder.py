import os
import re
import sys
import chromadb
import numpy as np
import plotly.express as px
from sklearn.decomposition import PCA
from tree_sitter import Language, Parser
import tree_sitter_python as tspython
from sentence_transformers import SentenceTransformer

# Add the source directory to sys.path to import context_compressor
sys.path.append("./mllm/src")
from mllm.data.context_compressor import context_clean_compress

# --- Configuration ---
REPO_ROOT = "./mllm"
DB_PATH = "./.cli_memory"
COLLECTION_NAME = "mllm_context"
EMBED_MODEL_NAME = "nomic-ai/nomic-embed-text-v1"

# Initialize Tree-Sitter
print(f"[INIT] Loading Tree-Sitter Python language grammar...")
PY_LANGUAGE = Language(tspython.language())
parser = Parser(PY_LANGUAGE)
print(f"[INIT] Parser initialized for Python AST extraction.")

# Initialize Embedding Model
print(f"[INIT] Loading Embedding Model: {EMBED_MODEL_NAME}...")
# Nomic models often require trust_remote_code=True for their custom pooling logic
model = SentenceTransformer(EMBED_MODEL_NAME, trust_remote_code=True)
print(f"[INIT] Model loaded successfully.")

def _get_node_name(node, content):
    """Helper to extract class or function name from AST node."""
    for child in node.children:
        if child.type == 'identifier':
            return content[child.start_byte:child.end_byte].decode('utf-8')
    return "unknown"

def parse_python_ast(file_path):
    """Scans .py files and returns a list of unbroken code chunks corresponding to structural boundaries."""
    print(f"[AST] Parsing file: {file_path}")
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
        tree = parser.parse(content)
        root_node = tree.root_node
        
        chunks = []
        for child in root_node.children:
            # We target top-level definitions to preserve functional logic
            if child.type in ['function_definition', 'class_definition']:
                code = content[child.start_byte:child.end_byte].decode('utf-8')
                name = _get_node_name(child, content)
                print(f"[AST] Found {child.type}: {name}")
                chunks.append({
                    'content': code,
                    'metadata': {
                        'type': 'code',
                        'node_type': child.type,
                        'file_path': file_path,
                        'name': name
                    }
                })
        return chunks
    except Exception as e:
        print(f"[ERROR] Failed to parse {file_path}: {e}")
        return []

import hashlib
import json

def get_file_hash(file_path):
    """Calculates SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def sync_mllm_vectors():
    """Automates incremental indexing across the repository."""
    print(f"[SYNC] Initializing ChromaDB at {DB_PATH}...")
    client = chromadb.PersistentClient(path=DB_PATH)
    collection = client.get_or_create_collection(name=COLLECTION_NAME)
    
    hash_file = os.path.join(DB_PATH, "file_hashes.json")
    if os.path.exists(hash_file):
        with open(hash_file, 'r') as f:
            file_hashes = json.load(f)
    else:
        file_hashes = {}
    
    new_hashes = {}
    all_chunks = []
    print(f"[SYNC] Scanning repository root: {REPO_ROOT}")
    
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for file in files:
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, REPO_ROOT)
            
            if file.endswith((".py", ".md")):
                current_hash = get_file_hash(file_path)
                if file_hashes.get(rel_path) == current_hash:
                    print(f"[SKIP] File unchanged: {rel_path}")
                    new_hashes[rel_path] = current_hash
                    continue
                
                print(f"[SYNC] Processing modified file: {rel_path}")
                new_hashes[rel_path] = current_hash
                
                if file.endswith(".py"):
                    all_chunks.extend(parse_python_ast(file_path))
                else:
                    with open(file_path, 'r') as f:
                        content = f.read()
                    compressed = context_clean_compress(content)
                    md_blocks = compressed.split("\n\n")
                    for i, block in enumerate(md_blocks):
                        if len(block.strip()) > 100:
                            all_chunks.append({
                                'content': block.strip(),
                                'metadata': {'type': 'docs', 'file_path': file_path, 'chunk_index': i}
                            })
    
    if not all_chunks:
        print(f"[SYNC] No changes detected. Index up-to-date.")
        return

    print(f"[EMBED] Vectorizing {len(all_chunks)} chunks...")
    ids = [f"{c['metadata'].get('name', 'chunk')}_{i}_{hash(c['content'])}" for i, c in enumerate(all_chunks)]
    documents = [c['content'] for c in all_chunks]
    metadatas = [c['metadata'] for c in all_chunks]
    prefixed_docs = ["search_document: " + doc for doc in documents]
    
    # Batch processing with size=1 for M1 Max memory safety
    embeddings = []
    for doc in prefixed_docs:
        embeddings.append(model.encode(doc, batch_size=1).tolist())
    
    collection.upsert(ids=ids, documents=documents, metadatas=metadatas, embeddings=embeddings)
    
    with open(hash_file, 'w') as f:
        json.dump(new_hashes, f)
    print(f"[DONE] Sovereign Embedder sync complete. Vectors indexed: {len(all_chunks)}")

from transformers import pipeline

# Initialize local lightweight generator for HyDE
# Using a small, fast model for zero-shot query expansion
print(f"[INIT] Loading HyDE Generator pipeline...")
generator = pipeline("text-generation", model="google/flan-t5-small")
print(f"[INIT] HyDE Generator initialized.")

def generate_hyde_query(query: str) -> str:
    """Generates a hypothetical answer to the query for better semantic retrieval."""
    print(f"[HYDE] Expanding query: {query}")
    prompt = f"Write a brief technical answer or code snippet answering this query: {query}"
    # Use flan-t5 for lightning fast generation
    expanded = generator(prompt, max_length=128, do_sample=True, temperature=0.7)[0]['generated_text']
    print(f"[HYDE] Expanded Query: {expanded}")
    return expanded

from rich.console import Console
from rich.table import Table

console = Console()

def search_collection(query: str, top_k: int = 5):
    """Retrieves chunks using HyDE expansion."""
    hyde_query = generate_hyde_query(query)
    client = chromadb.PersistentClient(path=DB_PATH)
    collection = client.get_collection(name=COLLECTION_NAME)
    
    # Embed the expanded query (prefixed with search_query for Nomic)
    embedding = model.encode("search_query: " + hyde_query, batch_size=1).tolist()
    
    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k,
        include=["documents", "metadatas"]
    )
    return results

def audit_retrieve(query: str, top_k: int = 5):
    """Executes a dry-run retrieval and presents an audit table."""
    console.print(f"[bold cyan]🔍 Auditing retrieval for:[/bold cyan] {query}")
    results = search_collection(query, top_k)
    
    table = Table(title="Retrieval Context Audit")
    table.add_column("Rank", style="dim")
    table.add_column("Type", style="green")
    table.add_column("Metadata", style="yellow")
    table.add_column("Content Preview", style="white")
    
    for i in range(len(results['documents'][0])):
        meta = results['metadatas'][0][i]
        doc = results['documents'][0][i]
        
        file_name = os.path.basename(meta.get('file_path', 'unknown'))
        meta_str = f"{file_name} ({meta.get('node_type', 'chunk')})"
        preview = (doc[:100] + '...') if len(doc) > 100 else doc
        
        table.add_row(str(i+1), meta.get('type', 'N/A'), meta_str, preview)
    
    console.print(table)
    return results

if __name__ == "__main__":
    import argparse
    parser_cli = argparse.ArgumentParser(description="Sovereign Embedder for mllm repository")
    parser_cli.add_argument("--sync", action="store_true", help="Sync repository to vector DB")
    parser_cli.add_argument("--visualize", action="store_true", help="Visualize vector space")
    parser_cli.add_argument("--audit", type=str, help="Dry-run retrieval audit for a query")
    args = parser_cli.parse_args()
    
    if args.sync:
        sync_mllm_vectors()
    elif args.visualize:
        visualize_mllm_codebase_plotly()
    elif args.audit:
        audit_retrieve(args.audit)
    else:
        parser_cli.print_help()
