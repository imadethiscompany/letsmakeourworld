## AI Framework Installer Automation Artifact

Below is a minimal Python script that automates the installation of popular AI frameworks such as **ComfyUI**, **Ollama**, and **OpenWebUI**. It downloads the latest releases, extracts them, and sets up system services where applicable.

```python
#!/usr/bin/env python3
import os, subprocess, sys, urllib.request, tarfile, zipfile

def run(cmd):
    subprocess.check_call(cmd, shell=True)

def download(url, dest):
    print(f'Downloading {url}...')
    urllib.request.urlretrieve(url, dest)

def extract(archive, target):
    if archive.endswith('.tar.gz') or archive.endswith('.tgz'):
        with tarfile.open(archive, 'r:gz') as tar:
            tar.extractall(path=target)
    elif archive.endswith('.zip'):
        with zipfile.ZipFile(archive, 'r') as zip_ref:
            zip_ref.extractall(target)
    else:
        raise ValueError('Unsupported archive format')

def install_comfyui():
    url = 'https://github.com/comfyanonymous/ComfyUI/releases/latest/download/ComfyUI-linux-x86_64.tar.gz'
    dest = '/tmp/comfyui.tar.gz'
    download(url, dest)
    extract(dest, '/opt/comfyui')
    run('chmod +x /opt/comfyui/run.sh')
    print('ComfyUI installed at /opt/comfyui')

def install_ollama():
    url = 'https://github.com/ollama/ollama/releases/latest/download/ollama-linux-amd64.tar.gz'
    dest = '/tmp/ollama.tar.gz'
    download(url, dest)
    extract(dest, '/opt/ollama')
    run('chmod +x /opt/ollama/ollama')
    print('Ollama installed at /opt/ollama')

def install_openwebui():
    # OpenWebUI is Docker‑based; we provide a simple docker‑compose snippet
    compose = '''
version: "3"
services:
  openwebui:
    image: ghcr.io/open-webui/open-webui:latest
    ports:
      - "3000:8080"
    environment:
      - OLLAMA_API_URL=http://host.docker.internal:11434
    restart: unless‑stopped
'''
    os.makedirs('/opt/openwebui', exist_ok=True)
    with open('/opt/openwebui/docker-compose.yml', 'w') as f:
        f.write(compose)
    print('OpenWebUI docker-compose written to /opt/openwebui')

if __name__ == '__main__':
    actions = {
        'comfyui': install_comfyui,
        'ollama': install_ollama,
        'openwebui': install_openwebui,
    }
    for name, func in actions.items():
        try:
            func()
        except Exception as e:
            print(f'Failed to install {name}: {e}', file=sys.stderr)
```

Save this script as `install_ai_frameworks.py`, make it executable (`chmod +x install_ai_frameworks.py`), and run it with root privileges. It will place the frameworks under `/opt` and provide a ready‑to‑use Docker‑Compose file for OpenWebUI.
