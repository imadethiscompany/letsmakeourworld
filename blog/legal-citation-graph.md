# Automatic Construction of a Legal Citation Graph

This minimal automation artifact demonstrates how to start building a citation graph from a large collection of Ukrainian court decisions.

```python
import os
import json
from pathlib import Path

# Placeholder: path to the directory containing court decision text files
DATA_DIR = Path(os.getenv("COURT_DATA_DIR", "/data/ukraine_courts"))

def extract_citations(text: str) -> list:
    """Very naive citation extractor – looks for patterns like 'Case No. XYZ'"""
    import re
    pattern = r"Case\s+No\.\s+\w+"
    return re.findall(pattern, text)

def build_graph():
    graph = {}
    for file_path in DATA_DIR.rglob("*.txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
        citations = extract_citations(text)
        graph[str(file_path)] = citations
    # Save as JSON for downstream processing
    out_path = Path("citation_graph.json")
    out_path.write_text(json.dumps(graph, ensure_ascii=False, indent=2))
    print(f"Citation graph written to {out_path}")

if __name__ == "__main__":
    build_graph()
```

*This script is intentionally minimal and serves as a starting point. It can be expanded with proper NLP parsing, database storage, and graph analysis tools.*
