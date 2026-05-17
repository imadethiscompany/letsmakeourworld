# Vivago Video Agent Automation

This minimal automation artifact provides a simple API endpoint to generate a video using the ProVideoEngine.

```python
# vivago_video_agent.py
from execution.pro_video_engine import ProVideoEngine

def generate_video(topic, niche="tech", duration=45):
    engine = ProVideoEngine()
    result = engine.create_video(topic=topic, niche=niche, duration=duration)
    return result
```

Deploy this script on the serverless platform to trigger video creation.
