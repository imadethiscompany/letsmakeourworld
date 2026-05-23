# Canva for AI Training - Minimal Automation Artifact

This page provides a minimal automation script that demonstrates a simple "Canva for AI training" concept. The script allows users to define a drag‑and‑drop style pipeline for training a small image classifier.

```python
# canva_ai_training.py
import json
from pathlib import Path

def create_training_pipeline(config_path: str, output_path: str):
    """Create a simple training pipeline definition.
    Args:
        config_path: Path to a JSON config describing datasets and model.
        output_path: Where to write the generated pipeline script.
    """
    with open(config_path) as f:
        cfg = json.load(f)
    # Generate a minimal training script
    script = f"""import json\nfrom pathlib import Path\n\n# Load config\nwith open('{config_path}') as f:\n    cfg = json.load(f)\n\n# Placeholder training logic\nprint('Training model', cfg.get('model'))\nprint('Using dataset', cfg.get('dataset'))\n# ... actual training code would go here ...\n\n# Save dummy model\nPath('{output_path}').write_text('dummy model data')\n"""
    Path(output_path).write_text(script)
    print(f'Pipeline script written to {output_path}')
\nif __name__ == "__main__":
    import argparse\n    parser = argparse.ArgumentParser(description='Generate a training pipeline script')\n    parser.add_argument('--config', required=True, help='Path to config JSON')\n    parser.add_argument('--out', required=True, help='Output script path')\n    args = parser.parse_args()\n    create_training_pipeline(args.config, args.out)\n```

**How to use**
1. Create a `config.json` describing your model and dataset, e.g.:
```json
{\n  "model": "simple_cnn",\n  "dataset": "cats_vs_dogs"\n}\n```
2. Run the script:
```
python canva_ai_training.py --config config.json --out train.py
```
3. The generated `train.py` is a ready‑to‑run placeholder you can extend.

---
*This minimal artifact showcases the idea of a drag‑and‑drop pipeline generator for AI training.*
