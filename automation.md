# TabPFN-MT Automation Artifact

## Overview

**TabPFN-MT** is a natively multitask in‑context learner for tabular data. This minimal automation artifact provides a ready‑to‑run Python script that demonstrates loading a pretrained TabPFN‑MT model and making predictions on a sample CSV.

## Files

- `tabpfn_mt_demo.py` – simple script using the `tabpfn` library.
- `requirements.txt` – required dependencies.

### `tabpfn_mt_demo.py`
```python
import pandas as pd
from tabpfn import TabPFNClassifier

# Sample data (replace with your own CSV)
csv_path = "sample_data.csv"
df = pd.read_csv(csv_path)
X = df.drop(columns=["target"]).values
y = df["target"].values

# Initialize TabPFN‑MT classifier (default hyper‑parameters)
clf = TabPFNClassifier()
clf.fit(X, y)

# Predict on the same data (for demo)
pred = clf.predict(X)
print("Predictions:", pred[:10])
```

### `requirements.txt`
```
pandas
tabpfn
```

## Usage
```bash
pip install -r requirements.txt
python tabpfn_mt_demo.py
```

This script can be extended to load any tabular dataset and perform multitask learning.
