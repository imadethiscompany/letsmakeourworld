# StoreClaw Automation Artifact

This minimal automation artifact demonstrates a simple Python script that fetches leads for StoreClaw and sends a notification email.

```python
import json
from find_leads import find_leads
from send_email import send_email

leads = find_leads(query='ecommerce stores', limit=5)
body = "Top leads for StoreClaw:\n" + json.dumps(leads, indent=2)
send_email(to='team@storeclaw.com', subject='StoreClaw Leads', body=body)
```

Deploy this script to your automation folder and integrate with your workflow.