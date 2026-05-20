# Clouted Viral Video Automation

This minimal automation artifact provides a simple Python script that leverages the ProVideoEngine to generate a short video designed to go viral.

```python
# automation/clouted_viral_video.py
from execution.pro_video_engine import ProVideoEngine

engine = ProVideoEngine()
result = engine.create_video(
    topic="How to Make Short Videos Go Viral",
    niche="tech",
    duration=45,
)
print("Video saved to:", result["video_path"])
print("Metadata:", result["metadata"])
```

Save this script in your project and run it to generate a ready‑to‑publish video.
