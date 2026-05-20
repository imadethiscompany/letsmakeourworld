# Airbnb Hotels AI Automation

This minimal automation artifact demonstrates a simple webhook integration that could be used to onboard new Airbnb hotel hosts using AI.

```python
import requests

def onboard_host(host_name, email):
    payload = {
        "name": host_name,
        "email": email,
        "onboard": True,
        "use_ai": True
    }
    response = requests.post("https://api.airbnb.com/host/onboard", json=payload)
    return response.json()

# Example usage
if __name__ == "__main__":
    result = onboard_host("John Doe", "john@example.com")
    print(result)
```

Deploy this script as part of your backend to automate host onboarding with AI assistance.
