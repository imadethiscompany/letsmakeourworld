# AI Camera Controversy Automation

This minimal automation sends a payment link to interested leads.

```python
import os
from utils import send_email

PAYMENT_LINK = "https://buy.stripe.com/test_8x24grahR2kAePx4QGc7D3f"

def notify_lead(email, name):
    subject = "AI Camera Controversy Report – Purchase Link"
    body = f"Hi {name},\n\nThank you for your interest. You can purchase the report here: {PAYMENT_LINK}\n\nBest regards,\nTeam"
    send_email(to=email, subject=subject, body=body)
```