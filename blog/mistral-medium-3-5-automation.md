# Automation Artifact

This page documents the minimal automation artifact for **Mistral Medium 3.5**. It includes a simple Python script that can be used to trigger a payment link generation or other automated tasks.

```python
import requests

# Example: Open the Stripe payment link (replace with your actual link)
PAYMENT_LINK = "https://buy.stripe.com/test_6oUbIT1Ll0csazh5UKc7x3e"

def open_payment_link():
    response = requests.get(PAYMENT_LINK)
    print('Opened payment link, status:', response.status_code)

if __name__ == "__main__":
    open_payment_link()
```

Deploy this script as part of your CI/CD pipeline or run manually to verify the payment flow.
