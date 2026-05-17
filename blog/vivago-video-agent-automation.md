# Vivago Video Agent Automation

```python
"""Minimal automation for Vivago Video Agent.
Publishes product, finds leads, and emails payment link.
"""
import os

# Publish product (Stripe & website)
product = publish_product(
    name="Vivago Video Agent",
    description="AI-powered video creation service.",
    price_cents=9900,
    category="automation",
    features=["AI video generation", "Custom branding", "Fast turnaround"]
)

# Find 10 high‑intent leads (local businesses)
leads = find_leads(query="video production services in New York", limit=10)

# Create payment link
payment = create_payment_link(price_id=product.get("price_id"))

# Send email to each lead with CTA
for lead in leads:
    send_email(
        to=lead["email"],
        subject="Boost Your Business with AI Video",
        body=f"Hi {lead['name']},\n\nCheck out our Vivago Video Agent: {payment.get('url')}\n\nBest,\nTeam"
    )
```