# Hackers Exploit cPanel Bug – Protect Your Websites

**Summary:**
Recent reports indicate that attackers are still exploiting a critical vulnerability in cPanel to gain unauthorized access to thousands of websites. This automation artifact provides a concise guide and a ready‑to‑use script to scan your servers for the vulnerable version and apply immediate mitigations.

## What You Need
- Access to your server via SSH
- cPanel version check (`/usr/local/cpanel/version`)
- Ability to update cPanel (`/scripts/upcp`)

## Quick Scan Script (Python)
```python
#!/usr/bin/env python3
import subprocess, sys, re

def get_cpanel_version():
    try:
        out = subprocess.check_output(["/usr/local/cpanel/version"], text=True).strip()
        return out
    except Exception as e:
        print("Error retrieving cPanel version:", e)
        sys.exit(1)

def is_vulnerable(version):
    # Vulnerable versions: 106 to 108 (example range)
    match = re.match(r"(\d+)", version)
    if not match:
        return False
    major = int(match.group(1))
    return 106 <= major <= 108

if __name__ == "__main__":
    ver = get_cpanel_version()
    print(f"cPanel version detected: {ver}")
    if is_vulnerable(ver):
        print("⚠️ Your cPanel version is vulnerable! Run '/scripts/upcp' to update immediately.")
    else:
        print("✅ Your cPanel version is not in the vulnerable range.")
```

## Immediate Steps
1. **Run the script** on each server.
2. If vulnerable, execute:
   ```bash
   /scripts/upcp
   ```
3. Verify the update and restart services.

---
*Stay protected – monitor your infrastructure continuously.*