# CVE-2024-YIKES Automation Script

This minimal automation artifact fetches details for CVE-2024-YIKES from the NVD API and outputs a concise report.

```python
import requests, json, sys

def fetch_cve(cve_id: str):
    url = f"https://services.nvd.nist.gov/rest/json/cve/1.0/{cve_id}"
    resp = requests.get(url, timeout=10)
    if resp.status_code != 200:
        print(f"Failed to fetch CVE data: {resp.status_code}")
        sys.exit(1)
    return resp.json()

def summarize(cve_data):
    cve = cve_data.get('result', {}).get('CVE_Items', [])[0]
    meta = cve.get('cve', {})
    description = meta.get('description', {}).get('description_data', [{}])[0].get('value', 'N/A')
    severity = cve.get('impact', {}).get('baseMetricV3', {}).get('cvssV3', {}).get('baseSeverity', 'N/A')
    print(f"CVE ID: {meta.get('CVE_data_meta', {}).get('ID', 'N/A')}")
    print(f"Description: {description}")
    print(f"Severity: {severity}")

if __name__ == "__main__":
    cve_id = "CVE-2024-YIKES"
    data = fetch_cve(cve_id)
    summarize(data)
```

*Save this script as `cve_yikes_report.py` and run with `python cve_yikes_report.py`.*