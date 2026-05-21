# Operationalizing Document AI

A minimal automation artifact that demonstrates a simple OCR + LLM pipeline.

```python
import requests
from io import BytesIO
from PIL import Image
import pytesseract

# Sample image URL (placeholder)
image_url = "https://example.com/sample-doc.png"
img_data = requests.get(image_url).content
image = Image.open(BytesIO(img_data))

# OCR
text = pytesseract.image_to_string(image)
print("Extracted Text:", text)

# Simple LLM call (placeholder)
response = requests.post(
    "https://api.example-llm.com/v1/completions",
    json={"prompt": text, "max_tokens": 100},
    headers={"Authorization": "Bearer YOUR_API_KEY"},
)
print("LLM Response:", response.json())
```

This script pulls an image, runs OCR via Tesseract, and sends the extracted text to an LLM endpoint.

*Deploy this script in your own environment to start processing documents automatically.*