# Vivago Video Agent Automation

This page contains a minimal automation script for the **Vivago Video Agent**. The script demonstrates how to publish the product, find leads, and send a follow‑up email with a payment link.

```python
from automation_tools import publish_product, find_leads, create_payment_link, send_email

# 1. Publish the product on Stripe and website
product = publish_product(
    name="Vivago Video Agent",
    description="AI‑powered video creation service for businesses.",
    price_cents=19900,
    category="automation",
    features=[
        "AI script generation",
        "Voice cloning",
        "Remotion motion graphics",
        "One‑click rendering",
    ],
)

# 2. Find 10 high‑intent leads (local businesses)
leads = find_leads(query="marketing agencies in San Francisco", limit=10)

# 3. Create a payment link for the product
payment = create_payment_link(product_name=product["name"], price_cents=19900)

# 4. Send an email to each lead with the payment link
for lead in leads:
    send_email(
        to=lead["email"],
        subject="Boost Your Marketing with AI‑Generated Videos",
        body=f"Hi {lead['name']},\n\nCheck out our Vivago Video Agent service: {payment['url']}\n\nBest,\nThe Vivago Team",
    )
```

*Deploy this script as needed to automate your sales funnel.*
