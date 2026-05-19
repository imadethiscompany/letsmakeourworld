# Automation Artifact: Refresh AI Ranking

This minimal script fetches a list of open‑source AI agents and foundation models from a public API and updates the ranking JSON used by the live ranking page.

```python
import json, requests

API_URL = "https://huggingface.co/api/models"

def fetch_models():
    resp = requests.get(API_URL)
    resp.raise_for_status()
    data = resp.json()
    # Filter for open‑source models only (example condition)
    open_models = [m for m in data if not m.get('private', True)]
    # Simplify fields
    ranking = [{
        "id": m["id"],
        "downloads": m.get("downloads", 0),
        "likes": m.get("likes", 0)
    } for m in open_models]
    # Sort by downloads descending
    ranking.sort(key=lambda x: x["downloads"], reverse=True)
    return ranking

if __name__ == "__main__":
    ranking = fetch_models()
    with open("data/ranking.json", "w") as f:
        json.dump(ranking, f, indent=2)
    print("Ranking updated,", len(ranking), "models")
```

Add this script to `automation/refresh_ranking.py` in the repo and set up a scheduled Vercel build to run it before each deployment.
