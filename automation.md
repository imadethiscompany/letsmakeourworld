# White House AI Model Review Automation

This minimal automation fetches the latest White House briefing on AI model review and outputs the headline.

```python
import requests

def fetch_brief():
    url = "https://www.whitehouse.gov/briefings/ai-model-review"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        # Simple extraction of title tag
        start = resp.text.find('<title>')
        end = resp.text.find('</title>', start)
        title = resp.text[start+7:end].strip() if start != -1 else 'No title found'
        print('Brief Title:', title)
    except Exception as e:
        print('Error fetching brief:', e)

if __name__ == "__main__":
    fetch_brief()
```
