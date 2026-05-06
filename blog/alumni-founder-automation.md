# Alumni Founder Automation

This minimal automation artifact helps Alumni Founder collect leads and send a payment link.

```python
import requests

def send_payment_link(email, link):
    # Simple email send via placeholder API
    payload = {
        "to": email,
        "subject": "Your Alumni Founder Payment Link",
        "body": f"Please complete your purchase: {link}"
    }
    # Replace with real email service endpoint
    response = requests.post("https://api.example.com/send_email", json=payload)
    return response.status_code

if __name__ == "__main__":
    # Example usage
    lead_email = "lead@example.com"
    payment_link = "https://pay.example.com/alumni-founder"
    status = send_payment_link(lead_email, payment_link)
    print("Email sent, status", status)
```
