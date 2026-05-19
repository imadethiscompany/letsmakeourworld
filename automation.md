# Llama.cpp Minimal Automation Artifact

This script automates the download, build, and a simple benchmark run for the **ggml-org/llama.cpp** repository.

```bash
#!/usr/bin/env bash
# Minimal automation for llama.cpp
set -e

# Clone repository
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp

# Build the project (requires make and a C++ compiler)
make

# Run a quick benchmark (generates a short text)
./main -m models/7B/ggml-model-q4_0.bin -n 128 -p "Once upon a time"
```

Save this script as `run_llama.sh`, make it executable (`chmod +x run_llama.sh`), and execute it to see llama.cpp in action.

---
*Automation artifact for internal use.*