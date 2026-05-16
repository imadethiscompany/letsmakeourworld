# Δ-Mem Automation Artifact

## Overview
This minimal automation artifact demonstrates how to integrate **Δ-Mem: Efficient Online Memory for Large Language Models** into a Python workflow.

## Sample Script (`delta_mem_demo.py`)
```python
import requests

API_URL = "https://api.delta-mem.example.com/v1/memory"

# Simple function to store a snippet and retrieve it later
def store_and_query(key: str, value: str):
    # Store the value
    store_resp = requests.post(f"{API_URL}/store", json={"key": key, "value": value})
    store_resp.raise_for_status()
    # Query the value
    query_resp = requests.get(f"{API_URL}/query", params={"key": key})
    query_resp.raise_for_status()
    return query_resp.json()["value"]

if __name__ == "__main__":
    result = store_and_query("greeting", "Hello from Δ‑Mem!")
    print("Retrieved:", result)
```

## How to Use
1. Install the required dependency:
```bash
pip install requests
```
2. Replace `API_URL` with your deployed Δ‑Mem endpoint.
3. Run the script:
```bash
python delta_mem_demo.py
```

This artifact can be extended to batch processing, streaming, or integration with LLM inference pipelines.

---
*Created automatically by Multica for the Δ‑Mem product launch.*