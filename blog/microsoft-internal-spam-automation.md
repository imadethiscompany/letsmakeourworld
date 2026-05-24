# Scammers Abuse Internal Microsoft Account

**Problem:** Threat actors are leveraging a compromised internal Microsoft account to send phishing spam links to employees, increasing risk of credential theft.

**Solution:** Deploy an automated monitoring script that:
1. Uses Microsoft Graph API to watch sent messages from the internal account.
2. Flags any outbound messages containing URLs not in an allowlist.
3. Sends real‑time alerts to security SOC via Teams webhook.
4. Auto‑revokes the compromised account token.

**Minimal Automation Artifact** (Python script):
```python
import os, re, requests
from msgraph.core import GraphClient

ALLOWLIST = {"microsoft.com", "contoso.com"}

client = GraphClient(credential=os.getenv("GRAPH_TOKEN"))

def is_suspicious(url):
    domain = re.findall(r"https?://([^/]+)/?", url)[0].lower()
    return domain not in ALLOWLIST

messages = client.get('/users/{user_id}/messages?$filter=isRead eq false')
for msg in messages.json().get('value', []):
    for link in re.findall(r"https?://\S+", msg['body']['content']):
        if is_suspicious(link):
            requests.post(os.getenv('TEAMS_WEBHOOK'), json={"text": f"Suspicious link detected: {link}"})
            client.post(f"/users/{{user_id}}/revokeSignInSessions")
            break
```

Deploy this script as a scheduled Azure Function or GitHub Action.

---
*Ready to protect your organization.*