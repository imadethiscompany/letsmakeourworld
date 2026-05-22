# iPromise Automation Artifact

This minimal automation script creates a Stripe product for iPromise and sends a confirmation email.

```python
import os
from some_module import publish_product, send_email

# Create product
product = publish_product(
    name="iPromise Subscription",
    description="Access to iPromise platform",
    price_cents=9900,
    category="automation",
    features=["Full access", "Priority support"]
)

# Send email
send_email(
    to="customer@example.com",
    subject="Your iPromise Subscription",
    body=f"Your product is ready: {product['url']}"
)
```