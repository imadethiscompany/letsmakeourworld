# Silk Quickstart

Silk is an open‑source cooperative fiber scheduler for Python.

## Install
```bash
pip install silk-scheduler
```

## Minimal Example
```python
import silk

# Create a scheduler
scheduler = silk.Scheduler()

# Define a simple task
@scheduler.task
async def hello():
    print("Hello from Silk!")

# Run the scheduler
scheduler.run()
```

This script demonstrates creating a scheduler, defining an async task, and running it. For more details, visit the [Silk GitHub repo](https://github.com/yourorg/silk).