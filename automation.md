# Cal.com DIY Minimal Automation

This page provides a minimal automation artifact for the **Cal.com DIY Toolkit**.

## Simple Python script to send payment link via email
```python
import smtplib
from email.mime.text import MIMEText

PAYMENT_LINK = "https://buy.stripe.com/test_9B6dR13TtaR64aT82Sc7D0h"
RECIPIENT = "lead@example.com"

msg = MIMEText(f"Hi,\n\nCheck out our Cal.com DIY Toolkit here: {PAYMENT_LINK}\n\nBest regards")
msg["Subject"] = "Cal.com DIY Toolkit – Payment Link"
msg["From"] = "sales@yourcompany.com"
msg["To"] = RECIPIENT

with smtplib.SMTP("smtp.example.com", 587) as server:
    server.starttls()
    server.login("sales@yourcompany.com", "password")
    server.send_message(msg)
```

You can adapt this script to your email provider and run it as part of your outreach automation.
