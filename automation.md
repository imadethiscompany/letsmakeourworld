# Minimal Automation Artifact

```python
# book_ai_breakdown.py
"""Minimal automation to send a payment link email for the AI book breakdown product."""
import os
import smtplib
from email.message import EmailMessage

# Configuration (replace with real values or environment vars)
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.example.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
SMTP_USER = os.getenv('SMTP_USER', 'user@example.com')
SMTP_PASS = os.getenv('SMTP_PASS', 'password')
FROM_EMAIL = os.getenv('FROM_EMAIL', 'sales@example.com')
PAYMENT_LINK = os.getenv('PAYMENT_LINK', 'https://buy.stripe.com/example')

def send_payment_email(to_email, buyer_name):
    msg = EmailMessage()
    msg['Subject'] = 'Your Access to "Tried to Write a Book with AI for a Year"'
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email
    msg.set_content(f"Hi {buyer_name},\n\nThank you for your interest! You can complete the purchase here: {PAYMENT_LINK}\n\nBest,\nThe Team")
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)

if __name__ == '__main__':
    # Example usage
    send_payment_email('customer@example.com', 'Customer')
```