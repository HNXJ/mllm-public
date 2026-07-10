import tempfile
import sqlite3
import pandas as pd
from pathlib import Path
from jmllm.util.helpers import estimate_tokens
from jmllm.util.config.model_config import ModelProfile

def test_estimate_tokens():
    assert estimate_tokens("hello world") == 2
    assert estimate_tokens("") == 0
    assert estimate_tokens("a" * 40) == 10

def test_model_profile_provider():
    profile = ModelProfile(
        model_name="test-model",
        api_url="http://localhost:1234",
        provider="openai",
        response_format={"type": "json_object"}
    )
    assert profile.provider == "openai"
    assert profile.response_format == {"type": "json_object"}

def test_sqlite_export():
    with tempfile.TemporaryDirectory() as tmp_dir:
        db_path = Path(tmp_dir) / "test.db"
        df = pd.DataFrame([{"file": "test.pdf", "score": 90}])
        
        conn = sqlite3.connect(db_path)
        df.to_sql("evaluations", conn, if_exists="replace", index=False)
        conn.close()
        
        conn = sqlite3.connect(db_path)
        res = pd.read_sql_query("SELECT * FROM evaluations", conn)
        conn.close()
        
        assert len(res) == 1
        assert res.iloc[0]["score"] == 90
