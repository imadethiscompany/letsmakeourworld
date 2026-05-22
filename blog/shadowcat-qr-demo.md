# ShadowCat Automation Artifact

This is a minimal automation artifact for **Show HN: ShadowCat – file transfer through QR Codes in a Browser**.

It provides a simple web page that demonstrates generating a QR code for a file URL.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>ShadowCat QR Demo</title>
  <script src="https://cdn.jsdelivr.net/npm/qrcode@1.5.0/build/qrcode.min.js"></script>
</head>
<body>
  <h1>ShadowCat QR Demo</h1>
  <input type="text" id="url" placeholder="Enter file URL" style="width:300px;" />
  <button onclick="generate()">Generate QR</button>
  <div id="qr"></div>
  <script>
    function generate() {
      const url = document.getElementById('url').value;
      if (!url) return alert('Enter a URL');
      const qrDiv = document.getElementById('qr');
      qrDiv.innerHTML = '';
      QRCode.toCanvas(url, { width: 256 }, function (error, canvas) {
        if (error) console.error(error);
        else qrDiv.appendChild(canvas);
      });
    }
  </script>
</body>
</html>
```

You can host this page on the site and use it to generate QR codes for any file URL.
