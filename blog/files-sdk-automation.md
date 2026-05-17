# Files SDK Minimal Automation

This is a minimal automation artifact demonstrating how to use the **Files SDK** to upload a file to your storage bucket.

```python
import os
from files_sdk import FilesClient

# Initialize the client (replace with your API token)
client = FilesClient(api_token=os.getenv("FILES_API_TOKEN"))

# Path to the local file you want to upload
local_path = "./example.txt"

# Destination path in the Files storage
remote_path = "/uploads/example.txt"

# Perform the upload
with open(local_path, "rb") as f:
    client.upload_file(f, remote_path)

print(f"Uploaded {local_path} to {remote_path}")
```

Save this script as `upload_example.py`, set the `FILES_API_TOKEN` environment variable, and run it to upload a file.

---

*This page is an automation artifact for the Files SDK.*