# Gemini Enterprise Agent P Automation

This minimal automation artifact demonstrates a simple Python script that fetches the latest news about **Google replacing Vertex AI with Gemini Enterprise Agent P** and prints it.

```python
import requests

def fetch_news():
    url = "https://news.google.com/rss/search?q=Gemini+Enterprise+Agent+P"
    resp = requests.get(url)
    print(resp.text[:500])

if __name__ == "__main__":
    fetch_news()
```

You can clone the repository and run `python fetch_gemini_news.py` to see the output.
