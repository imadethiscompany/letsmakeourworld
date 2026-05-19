# Llama.cpp Minimal Automation Artifact

This repository includes a simple automation script that clones the `llama.cpp` repository, builds it, and runs a basic inference test.

```bash
#!/usr/bin/env bash
set -e

# Clone the repository
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp

# Build the project (requires make and a C++ compiler)
make

# Run a quick test (ensure the binary works)
./main -h
```

Save this script as `automation.sh` and run it on a Unix-like system with `bash` installed.
