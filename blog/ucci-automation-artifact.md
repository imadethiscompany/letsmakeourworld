# UCCI Automation Artifact

This minimal automation script demonstrates a simple cost‑optimal LLM cascade routing using calibrated uncertainty.

```python
"""UCCI: Calibrated Uncertainty for Cost‑Optimal LLM Cascade Routing

A minimal example that selects the cheapest LLM model that satisfies a target
uncertainty level. Models are defined by their cost per token and an uncertainty
score (lower is better).
"""
from typing import List, Tuple

# Example model catalog: (model_name, cost_per_token, uncertainty_score)
MODELS: List[Tuple[str, float, float]] = [
    ("gpt-4o-mini", 0.000015, 0.3),
    ("gpt-4o", 0.00003, 0.2),
    ("claude-3.5-sonnet", 0.000025, 0.25),
    ("gemma-2b", 0.000005, 0.5),
]

def select_model(target_uncertainty: float, max_budget: float) -> Tuple[str, float]:
    """Return the cheapest model that meets the target uncertainty and budget.

    Args:
        target_uncertainty: Maximum acceptable uncertainty score.
        max_budget: Maximum cost per token you are willing to pay.
    Returns:
        (model_name, cost_per_token) of the selected model.
        Raises ValueError if no model satisfies the constraints.
    """
    # Filter models by uncertainty and budget
    candidates = [
        (name, cost) for name, cost, unc in MODELS
        if unc <= target_uncertainty and cost <= max_budget
    ]
    if not candidates:
        raise ValueError("No model satisfies the given constraints")
    # Choose the cheapest among candidates
    return min(candidates, key=lambda x: x[1])

if __name__ == "__main__":
    # Example usage
    try:
        model, cost = select_model(target_uncertainty=0.28, max_budget=0.00003)
        print(f"Selected model: {model} at ${cost:.6f} per token")
    except ValueError as e:
        print(e)
```

Save this script as `ucci_routing.py` and run it with Python 3.11+.
