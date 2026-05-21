# l9gpu Minimal Automation Artifact

This page provides a minimal automation script for collecting GPU utilization and attributing it to workloads.

## Python script (requires `pynvml`)
```python
import json
from pynvml import *

nvmlInit()
deviceCount = nvmlDeviceGetCount()
metrics = []
for i in range(deviceCount):
    handle = nvmlDeviceGetHandleByIndex(i)
    name = nvmlDeviceGetName(handle).decode()
    util = nvmlDeviceGetUtilizationRates(handle)
    memInfo = nvmlDeviceGetMemoryInfo(handle)
    metrics.append({
        "gpu_index": i,
        "name": name,
        "gpu_util": util.gpu,
        "memory_util": util.memory,
        "memory_total_mb": memInfo.total // (1024 * 1024),
        "memory_used_mb": memInfo.used // (1024 * 1024),
    })

nvmlShutdown()
print(json.dumps(metrics, indent=2))
```

Run this script on any host with NVIDIA GPUs to get per‑GPU utilization data. Integrate it with your observability stack (Prometheus, Grafana, etc.) for workload‑level attribution.

---
*This artifact is part of the **l9gpu** open‑source project.*
