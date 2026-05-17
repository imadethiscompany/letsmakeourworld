# Automation Artifact

This minimal automation artifact provides a quick lead generation and email outreach script for the "Americans Are Smashing Flock Cameras" campaign.

```python
import json
from utils import find_leads, send_email

def run():
    leads = find_leads(query="camera repair services in USA", limit=5)
    for lead in leads:
        send_email(
            to=lead["email"],
            subject="Join the Flock Camera Movement",
            body="Hi {name},\n\nWe noticed your interest in cameras. Check out our initiative...".format(name=lead.get("name", ""))
        )
    print("Sent emails to", len(leads))

if __name__ == "__main__":
    run()
```

Deploy this script in your environment to start engaging leads instantly.
