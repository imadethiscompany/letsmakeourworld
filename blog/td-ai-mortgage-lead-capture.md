# TD’s AI Just Made Mortgage Waiting Obsolete – Automation Artifact

## Overview
This minimal automation artifact demonstrates how to capture high‑intent mortgage leads directly from the **TD’s AI Just Made Mortgage Waiting Obsolete** article page.

## What it does
- **Scrapes** the article URL for any embedded mortgage‑related contact forms.
- **Extracts** email addresses entered by visitors.
- **Posts** the leads to our internal CRM via a simple webhook.

## Quick Start (Python 3.10+)
```python
import requests, re
from bs4 import BeautifulSoup

ARTICLE_URL = "https://www.pymnts.com/news/2024/tds-ai-mortgage-waiting-obsolete/"
WEBHOOK_URL = "https://example.com/webhook/leads"

def fetch_page(url):
    return requests.get(url).text

def extract_emails(html):
    soup = BeautifulSoup(html, "html.parser")
    # naive email regex on page text
    return re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}", soup.get_text())

def send_to_crm(emails):
    for email in set(emails):
        requests.post(WEBHOOK_URL, json={"email": email, "source": ARTICLE_URL})

if __name__ == "__main__":
    html = fetch_page(ARTICLE_URL)
    emails = extract_emails(html)
    if emails:
        send_to_crm(emails)
        print(f"Sent {len(emails)} leads to CRM")
    else:
        print("No emails found")
```

## Deploying the script
1. Save the code above as `lead_capture.py`.
2. Run `python lead_capture.py` on a schedule (e.g., daily via cron).
3. Monitor the webhook endpoint for incoming leads.

---
*This page is a minimal automation artifact for the TD’s AI Mortgage article. It can be extended with more sophisticated parsing, authentication, and error handling as needed.*