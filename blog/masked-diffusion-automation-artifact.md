# Masked Diffusion Automation Artifact

We present a minimal Python automation script that demonstrates how to invoke a masked diffusion language model for text-based world modeling. This script is a starter template for researchers and developers.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load a placeholder model (replace with actual masked diffusion model)
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

prompt = "The world is a simulation where"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_length=50)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

*Replace `model_name` with the appropriate masked diffusion checkpoint.*

---

**Download**: The full script is available in the repository at `execution/minimal_artifact.py`.
