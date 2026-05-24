# DeepSeek Reasonix Automation Artifact

## Overview
A minimal automation script that demonstrates how to use the **DeepSeek Reasonix** native coding agent with high caching and low cost. The script provides a simple CLI wrapper to generate code snippets based on a prompt, leveraging the agent's caching layer to speed up repeated requests.

```python
import os
import json
import requests

# Simple DeepSeek Reasonix client
class ReasonixClient:
    def __init__(self, api_key: str, cache_dir: str = ".reasonix_cache"):
        self.api_key = api_key
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)

    def _cache_path(self, prompt: str) -> str:
        # deterministic cache filename
        safe = prompt.replace(" ", "_")[:100]
        return os.path.join(self.cache_dir, f"{safe}.json")

    def _load_cache(self, prompt: str):
        path = self._cache_path(prompt)
        if os.path.exists(path):
            with open(path, "r") as f:
                return json.load(f)
        return None

    def _save_cache(self, prompt: str, response: dict):
        path = self._cache_path(prompt)
        with open(path, "w") as f:
            json.dump(response, f)

    def generate(self, prompt: str) -> str:
        # Check cache first (high‑capacity caching)
        cached = self._load_cache(prompt)
        if cached:
            return cached["code"]
        # Call DeepSeek Reasonix API (placeholder endpoint)
        resp = requests.post(
            "https://api.deepseek.com/v1/reasonix",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={"prompt": prompt, "max_tokens": 500},
            timeout=15,
        )
        resp.raise_for_status()
        data = resp.json()
        code = data.get("code", "")
        # Store in cache for cheap subsequent calls
        self._save_cache(prompt, {"code": code})
        return code

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate code with DeepSeek Reasonix")
    parser.add_argument("prompt", help="Natural language description of the code you need")
    args = parser.parse_args()
    client = ReasonixClient(api_key=os.getenv("DEEPSEEK_API_KEY"))
    print(client.generate(args.prompt))
```

## How to Use
1. Set your DeepSeek API key:
   ```bash
   export DEEPSEEK_API_KEY=your_key_here
   ```
2. Run the script with a prompt:
   ```bash
   python reasonix_cli.py "Create a Python function that returns the Fibonacci sequence up to n"
   ```
   The first run contacts the API (low cost). Subsequent identical prompts are served from the local cache (free).

## Benefits
- **High‑capacity caching** reduces repeated token usage.
- **Low cost** thanks to cache‑first strategy.
- Minimal dependencies (only `requests`).
- Ready‑to‑run as a standalone CLI.

---
*This artifact is intentionally minimal to illustrate the core value proposition of DeepSeek Reasonix.*