# PollyReach Automation Artifact

This page showcases a minimal automation script for PollyReach. It includes a simple Python script that fetches leads and logs them.

```python
import json
from automation.pollyreach_leads import get_leads

leads = get_leads()
print(json.dumps(leads, indent=2))
```
