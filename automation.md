# Slideshot Automation

This page provides a minimal automation script for Slideshot.

```python
import requests

# Payment link for Slideshot
payment_link = "https://buy.stripe.com/test_eVq6ozblV0csazhbf4c7F0Z"

# Simple function to notify a buyer via email (placeholder)
def notify_buyer(email):
    # In real use, integrate with your email service
    print(f"Send email to {email} with link {payment_link}")

# Example usage
if __name__ == "__main__":
    test_emails = ["buyer1@example.com", "buyer2@example.com"]
    for e in test_emails:
        notify_buyer(e)
```

Deploy this script as part of your automation pipeline to quickly notify leads about the Slideshot product.
