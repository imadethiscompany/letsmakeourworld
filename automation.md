# InstaVM Automation Script

```python
"""Minimal automation for InstaVM.
Creates product, finds leads, sends email with payment link.
"""
import os

def main():
    # Publish product (placeholder values)
    product = {
        "name": "InstaVM",
        "description": "Instant VM provisioning service",
        "price_cents": 9900,
        "category": "automation",
        "features": ["Fast deployment", "Scalable", "Secure"]
    }
    # In real flow, call publish_product API here
    print("Product defined:", product)
    # Find leads (example query)
    leads_query = "tech startups in San Francisco"
    print(f"Would find leads for: {leads_query}")
    # Send email to a lead (placeholder)
    email = {
        "to": "lead@example.com",
        "subject": "InstaVM - Ready to provision your VMs",
        "body": "Hi,\n\nCheck out InstaVM here: https://instavm.example.com\n\nBest,\nTeam"
    }
    print("Would send email:", email)

if __name__ == "__main__":
    main()
```
