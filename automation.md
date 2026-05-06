# Alumni Founder Automation

A minimal automation script for the **Alumni Founder** product. This script creates a Stripe payment link for the product and sends an email to a lead.

```python
import os
from typing import Optional

# Placeholder functions – replace with real implementations or API calls

def create_payment_link(price_cents: int, product_name: str) -> Optional[str]:
    # In production, call the `create_payment_link` tool or Stripe API
    # Here we just simulate a URL
    return f"https://pay.stripe.com/pay/{product_name.replace(' ', '_')}_{price_cents}"

def send_email(to: str, subject: str, body: str) -> None:
    # In production, use the `send_email` tool
    print(f"Sending email to {to}\nSubject: {subject}\n\n{body}")

if __name__ == "__main__":
    product_name = "Alumni Founder"
    price_cents = 4900  # $49.00
    lead_email = os.getenv("LEAD_EMAIL", "lead@example.com")

    link = create_payment_link(price_cents, product_name)
    if link:
        subject = f"Your access to {product_name}"
        body = f"Hi there,\n\nThank you for your interest. Purchase your access here: {link}\n\nBest,\nTeam"
        send_email(lead_email, subject, body)
    else:
        print("Failed to create payment link")
```

Deploy this script as part of your automation pipeline.
