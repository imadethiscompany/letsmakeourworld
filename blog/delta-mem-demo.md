# Δ-Mem: Efficient Online Memory for Large Language Models

A minimal automation artifact: a simple Python script that demonstrates adding and retrieving a memory entry using the Δ-Mem library.

```python
from delta_mem import DeltaMem

# Initialize memory with a small capacity
mem = DeltaMem(max_size=10)

# Add a memory entry
mem.store('question', 'What is the capital of France?')
mem.store('answer', 'Paris')

# Retrieve the answer
print(mem.retrieve('question'))  # -> 'Paris'
```

You can copy this script and run it locally to see Δ-Mem in action.

[Download script](https://example.com/delta_mem_demo.py)
