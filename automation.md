# Automation Artifact for "The Economics of AI Inference: Inflation Dynamics, Welfare Costs, and Optimal Mo"

This minimal automation artifact is a simple Python script that fetches the latest price of GPU compute from a public API and prints a cost estimate for AI inference.

```python
import requests

def get_gpu_price():
    # Example API endpoint (placeholder)
    url = "https://api.example.com/gpu-price"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        return data.get('price_per_hour_usd')
    except Exception as e:
        print('Error fetching GPU price:', e)
        return None

def estimate_inference_cost(hours: float, usage_factor: float = 1.0):
    price = get_gpu_price()
    if price is None:
        return None
    return hours * usage_factor * price

if __name__ == "__main__":
    hours = 10
    cost = estimate_inference_cost(hours)
    if cost:
        print(f"Estimated cost for {hours} GPU hours: ${cost:.2f}")
    else:
        print("Could not estimate cost.")
```

You can clone the repository, locate this script in the `automation/` folder, and run it with Python 3.8+.
