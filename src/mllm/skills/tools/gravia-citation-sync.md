# gravia-citation-sync
Cross-references BibTeX with manuscripts/slides to ensure uniform scientific citation formatting.

## Protocol
1.  **Catalog:** Load `references.bib` or similar bibliography file.
2.  **Match:** Parse `index.html` or `manuscript.md` for citation tags (e.g., `[@CiteKey]`).
3.  **Format:** Generate formatted bibliography based on Biorxiv/PLOS standards.
4.  **Sync:** Update the "References" section in the presentation/document.
