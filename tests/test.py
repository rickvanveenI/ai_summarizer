import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module=".*importlib.*")

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_summarize_valid():
    response = client.post("/summarize", json={"text": "The quick brown fox jumps over the lazy dog."})
    assert response.status_code == 200
    data = response.json()
    assert data == {"summary": data["summary"]}
    assert isinstance(data["summary"], str)
    assert len(data["summary"]) > 0

def test_summarize_empty_text():
    response = client.post("/summarize", json={"text": ""})
    assert response.status_code == 400
    assert response.json()["detail"] == "Input text is required and must be a string."

def test_summarize_missing_text():
    response = client.post("/summarize", json={})
    assert response.status_code == 422
    errors = response.json()["detail"]
    assert isinstance(errors, list)
    assert any(
        "text" in e["loc"] and "Field required" in e["msg"]
        for e in errors
    )

def test_summarize_non_string():
    response = client.post("/summarize", json={"text": 12345})
    assert response.status_code == 422
    errors = response.json()["detail"]
    assert isinstance(errors, list)
    assert any(
        "text" in e["loc"] and "Input should be a valid string" in e["msg"]
        for e in errors
    )
