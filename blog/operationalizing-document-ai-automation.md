# Operationalizing Document AI Automation

## Minimal Automation Artifact

This artifact demonstrates a simple microservice that performs OCR on an uploaded document using Tesseract and then passes the extracted text to an LLM (OpenAI GPT) for summarization.

### `app.py`
```python
import os
from fastapi import FastAPI, File, UploadFile
import uvicorn
import pytesseract
from PIL import Image
import openai

app = FastAPI()

# Set your OpenAI API key as an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/process")
async def process_document(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    temp_path = f"/tmp/{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())
    # Perform OCR using Tesseract
    image = Image.open(temp_path)
    text = pytesseract.image_to_string(image)
    # Summarize using OpenAI GPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Summarize the following text:\n\n{text}"}],
        max_tokens=150,
    )
    summary = response['choices'][0]['message']['content']
    return {"summary": summary}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### How to Run
```bash
# Install dependencies
pip install fastapi uvicorn pillow pytesseract openai
# Ensure Tesseract OCR is installed on the system (e.g., apt-get install tesseract-ocr)
# Run the service
python app.py
```

Upload a document via `POST /process` and receive a concise summary.

---

*This minimal artifact can be extended into a full microservice architecture with Docker, Kubernetes, and async processing pipelines.*