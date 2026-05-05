# Agent Skills Automation Artifact

This minimal automation script allows you to publish the **Agent Skills** product, find 10 high‑intent leads, and send them a direct payment link via email.

```python
import os

# 1. Publish the product on Stripe and the website
product = publish_product(
    name="Agent Skills",
    description="Empower your team with AI‑driven agent capabilities.",
    price_cents=9900,
    category="automation",
    features=["Customizable agents", "Skill marketplace", "One‑click deployment"]
)

# 2. Find 10 leads (local businesses in major US cities)
leads = find_leads(query="local businesses in New York, Los Angeles, Chicago", limit=10)

# 3. Send each lead an email with the payment link
for lead in leads:
    send_email(
        to=lead["email"],
        subject="Unlock Agent Skills for Your Team",
        body=f"Hi {lead['name']},\n\nWe just launched Agent Skills. Grab it now: {product['payment_url']}\n\nBest,\nYour Team"
    )
```

Deploy this script to your automation repo and run it to start selling Agent Skills instantly.
