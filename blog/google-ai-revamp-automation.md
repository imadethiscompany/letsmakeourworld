# Google AI Revamp Automation

This minimal automation script fetches the Bloomberg article **"Google Revamps YouTube, Docs With Artificial Intelligence Tools"** and extracts the title and a short summary.

```python
import requests
from bs4 import BeautifulSoup

def fetch_article(url):
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    title = soup.find("h1").get_text(strip=True)
    paragraphs = soup.select("p")
    summary = " ".join(p.get_text(strip=True) for p in paragraphs[:3])
    return {"title": title, "summary": summary}

if __name__ == "__main__":
    url = "https://www.bloomberg.com/news/articles/2024-05-19/google-revamps-youtube-docs-with-ai-tools"
    data = fetch_article(url)
    print(f"Title: {data['title']}")
    print(f"Summary: {data['summary']}")
```

Save this script as `automation/google_ai_revamp.py` in the repository.
