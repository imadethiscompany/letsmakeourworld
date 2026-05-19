# AI Camera Controversy Automation

This minimal automation artifact provides a quick way to gather leads and send a payment link for the **AI Camera Controversy Report**.

- Run `find_leads` for "schools in Melbourne".
- Send email with Stripe payment link.

Use the following command snippet:
```bash
python - <<'PY'
from functions import find_leads, send_email
leads = find_leads(query='schools in Melbourne', limit=10)
for lead in leads:
    send_email(to=lead['email'], subject='AI Camera Report', body='Buy here: https://buy.stripe.com/test_8x24grahR2kAePx4QGc7D3f')
PY
```

Deploy this script in your automation environment to start converting leads instantly.
