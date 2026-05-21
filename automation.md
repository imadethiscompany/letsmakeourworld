# Colorado SB051 Automation Artifact

This minimal automation script checks if a given GitHub repository is excluded under the Colorado Amended SB051 Age Verification Bill (i.e., it contains an open‑source license). It can be used in CI pipelines.

```python
import sys, json, subprocess

def get_license(repo_path: str) -> str:
    """Return the SPDX identifier of the license if found, else empty string."""
    try:
        result = subprocess.check_output([
            "git", "-C", repo_path, "license"], stderr=subprocess.STDOUT)
        return result.decode().strip()
    except Exception:
        return ""

def is_excluded(repo_path: str) -> bool:
    """Return True if the repo is an open‑source project (has a license)."""
    license_id = get_license(repo_path)
    return bool(license_id)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: script.py <repo_path>"}))
        sys.exit(1)
    path = sys.argv[1]
    excluded = is_excluded(path)
    print(json.dumps({"repo_path": path, "excluded": excluded}))
```