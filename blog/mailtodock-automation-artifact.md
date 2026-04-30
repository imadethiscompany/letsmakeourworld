# MailToDock Automation Artifact

```python
# Minimal automation for MailToDock
# Publishes product, finds leads, emails them with a CTA

from utils import publish_product, find_leads, send_email

def run():
    product = publish_product(
        name="MailToDock",
        description="Digitize physical mail to your digital workspace.",
        price_cents=1999,
        category="automation",
        features=["Mail scanning", "Secure storage", "Instant access"]
    )
    payment_link = product["payment_link"]
    leads = find_leads(query="local businesses", limit=10)
    for lead in leads:
        email = lead.get("email") or "example@example.com"
        send_email(
            to=email,
            subject="Introducing MailToDock – Get Started Today!",
            body=f"Hi,\n\nCheck out MailToDock: {payment_link}\n\nBest,\nTeam"
        )

if __name__ == "__main__":
    run()
```
