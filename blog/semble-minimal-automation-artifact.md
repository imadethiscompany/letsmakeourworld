# Semble Minimal Automation Artifact

This is a minimal Python script that demonstrates how to invoke Semble for code search with dramatically reduced token usage.

```python
import subprocess
import sys

def search_semble(query, path="."):
    """Run Semble code search.
    Args:
        query (str): Search pattern.
        path (str): Directory to search.
    """
    # Assuming `semble` binary is installed and in PATH.
    # The `--tokens` flag reduces token usage (example placeholder).
    try:
        result = subprocess.check_output([
            "semble",
            "search",
            "--tokens",
            "0.02",
            query,
            "--path",
            path,
        ], text=True)
        print(result)
    except subprocess.CalledProcessError as e:
        print("Error running semble:", e, file=sys.stderr)
        sys.exit(e.returncode)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python semble_search.py <query> [path]", file=sys.stderr)
        sys.exit(1)
    q = sys.argv[1]
    p = sys.argv[2] if len(sys.argv) > 2 else "."
    search_semble(q, p)
```

Save this as `semble_search.py` in the repository root. You can then run:

```bash
python semble_search.py "def my_function" src/
```

This script is intentionally lightweight and serves as a starting point for building more complex automation around Semble.
