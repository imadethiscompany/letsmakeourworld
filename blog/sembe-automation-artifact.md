# Semble Automation Artifact

This is a minimal automation script for **Show HN: Semble – Code search for agents that uses 98% fewer tokens than grep**.

```python
import subprocess
import sys

def search_code(query, path="."):
    """Run Semble to search code with a natural language query.
    Requires `sembe` CLI to be installed and in PATH.
    """
    try:
        result = subprocess.check_output([
            "sembe", "search", "--query", query, "--path", path
        ], stderr=subprocess.STDOUT, text=True)
        print(result)
    except subprocess.CalledProcessError as e:
        print("Error running Semble:")
        print(e.output, file=sys.stderr)
        sys.exit(e.returncode)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python semblify.py <query> [path]")
        sys.exit(1)
    query = sys.argv[1]
    path = sys.argv[2] if len(sys.argv) > 2 else "."
    search_code(query, path)
```

Save this as `semblance.py` and run:

```bash
python semblance.py "find all TODO comments" ./my_project
```

This script demonstrates a simple wrapper around Semble to perform code searches with minimal token usage.
