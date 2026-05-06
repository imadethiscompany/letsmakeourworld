# Alumni Founder Automation Artifact

## Overview
This minimal automation artifact helps Alumni Founder quickly gather potential buyer leads and send them a payment link.

It consists of a single Python script `alumni_founder_automation.py` that:
1. Uses the **find_leads** tool to fetch 10 high‑intent leads.
2. Generates a Stripe payment link via **create_payment_link**.
3. Sends an email to each lead with a clear CTA.

---
```python
import json
from typing import List

# Placeholder functions – actual implementations are provided by the platform tools.

def get_leads() -> List[dict]:
    # In production this calls the platform's find_leads tool.
    # Here we just return a static example.
    return [
        {"name": "Acme Corp", "email": "contact@acme.com"},
        {"name": "Beta LLC", "email": "info@beta.com"},
        # ... up to 10 leads
    ]

def create_payment_link() -> str:
    # Calls create_payment_link tool – returns a URL string.
    return "https://buy.stripe.com/test_12345"

def send_email(to: str, subject: str, body: str):
    # Calls send_email tool.
    print(f"Sending to {to}")

def main():
    leads = get_leads()
    link = create_payment_link()
    subject = "Exclusive Alumni Founder Offer"
    for lead in leads:
        body = f"Hi {lead['name']},\n\nWe have a special offer for you. Purchase here: {link}\n\nBest,\nAlumni Founder Team"
        send_email(lead["email"], subject, body)

if __name__ == "__main__":
    main()
```

---
### How to Run
```bash
python alumni_founder_automation.py
```

Deploy this script as part of your automation pipeline or run locally.
