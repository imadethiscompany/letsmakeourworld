# Miami-Dade School Bus AI Ticketing Automation

This minimal automation artifact demonstrates a simple Python script that fetches the USA Today article and extracts key details.

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.usatoday.com/story/news/nation/2024/05/19/miami-dade-school-bus-ai-cameras-ticketing/"
resp = requests.get(url)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")
# Extract article title and first paragraph
title = soup.find('h1').get_text(strip=True)
first_para = soup.find('p').get_text(strip=True)
print('Title:', title)
print('Summary:', first_para)
```

Run this script locally to pull the latest article details.
