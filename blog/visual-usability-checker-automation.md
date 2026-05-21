# Visual Usability Checker Automation

A minimal automation script that captures a screenshot of a given URL, runs a simple visual diff against a baseline, and reports any differences.

## Script (Python)
```python
import sys
import subprocess
import argparse
from pathlib import Path

def capture(url: str, out_path: Path):
    # Use puppeteer via node to capture screenshot (requires node and puppeteer installed)
    cmd = ["node", "-e", f"const puppeteer = require('puppeteer'); (async () => {{ const browser = await puppeteer.launch(); const page = await browser.newPage(); await page.goto('{url}', {{waitUntil: 'networkidle2'}}); await page.screenshot({{path: '{out_path}'}}); await browser.close(); }})();"]
    subprocess.run(cmd, check=True)

def diff(img1: Path, img2: Path, diff_path: Path):
    # Use ImageMagick compare
    cmd = ["compare", "-metric", "AE", str(img1), str(img2), str(diff_path)]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    diff_pixels = result.stderr.strip()
    print(f"Different pixels: {diff_pixels}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Visual Usability Checker')
    parser.add_argument('url', help='URL to capture')
    parser.add_argument('--baseline', type=Path, required=True, help='Baseline image path')
    parser.add_argument('--output', type=Path, default=Path('screenshot.png'))
    parser.add_argument('--diff', type=Path, default=Path('diff.png'))
    args = parser.parse_args()
    capture(args.url, args.output)
    diff(args.baseline, args.output, args.diff)
```

## Usage
```bash
python visual_usability_checker.py https://example.com --baseline baseline.png
```

This script can be integrated into CI pipelines to automatically detect visual regressions.

---
*Built and deployed via automated workflow.*
