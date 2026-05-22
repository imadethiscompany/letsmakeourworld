# ShadowCat Minimal Automation

This is a minimal automation artifact for **Show HN: ShadowCat – file transfer through QR Codes in a Browser**. It provides a simple Python script that generates a QR code for a file URL, which can be scanned to download the file.

```python
import sys
import qrcode
import argparse

def generate_qr(url: str, output: str = "qr.png"):
    img = qrcode.make(url)
    img.save(output)
    print(f"QR code saved to {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate QR code for a file URL")
    parser.add_argument("url", help="URL of the file to share")
    parser.add_argument("-o", "--output", default="qr.png", help="Output image file")
    args = parser.parse_args()
    generate_qr(args.url, args.output)
```

Upload this script to your server, run it with the URL of the file you want to share, and distribute the generated `qr.png` to your users. Scanning the QR code will open the file URL in the browser, enabling easy file transfer without any additional software.

---
*Deploy this script anywhere you host your web services. The QR code can be displayed on a web page, printed, or shown in a terminal.*
