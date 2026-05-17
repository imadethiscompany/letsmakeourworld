# Automation Artifact: AI Debt Woes Script

```python
import requests
from bs4 import BeautifulSoup

def fetch_article(url):
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    title = soup.find('title').get_text(strip=True)
    # Simple summary: first 3 paragraphs
    paragraphs = soup.find_all('p')
    summary = '\n\n'.join(p.get_text(strip=True) for p in paragraphs[:3])
    return title, summary

if __name__ == "__main__":
    url = "https://www.japantimes.co.jp/news/2024/05/15/business/economy/ai-debt-wealthy-nations/"
    title, summary = fetch_article(url)
    print(f"Title: {title}\n\nSummary:\n{summary}")
```
