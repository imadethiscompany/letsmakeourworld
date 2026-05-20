# Owlish Minimal Automation Artifact

This is a minimal Python script that fetches 5 business leads for Owlish and prints them.

```python
import json
from functions import find_leads

def main():
    leads = find_leads(query="businesses interested in AI tools", limit=5)
    print(json.dumps(leads, indent=2))

if __name__ == "__main__":
    main()
```

Deploy this script as part of the Owlish automation suite.
