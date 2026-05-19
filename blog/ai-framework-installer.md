# AI Framework Installer

A minimal automation artifact that installs popular AI frameworks (ComfyUI, Ollama, OpenWebUI) via a simple Python script.

```python
import subprocess, sys

def install_framework(name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])

if __name__ == '__main__':
    for fw in ['comfyui', 'ollama', 'openwebui']:
        install_framework(fw)
```

The script is located at `automation/ai_framework_installer.py` in the repository.
