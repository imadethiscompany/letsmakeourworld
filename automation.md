# SOLAR Minimal Automation Artifact

## Overview
This artifact provides a concise description of a single API endpoint that enables the **Tool‑Augmented Agent for Closed‑loop Optimization, Simulation, and Modeling Orchestration**.

### Endpoint: `/api/run_simulation`
- **Method:** `POST`
- **Description:** Triggers a simulation run with the provided configuration.
- **Request Body (JSON):**
```json
{
  "simulation_id": "string",   // Unique identifier for the simulation
  "parameters": {                // Key‑value pairs of simulation parameters
    "duration": 60,            // in seconds
    "resolution": "high",
    "seed": 12345
  }
}
```
- **Response (JSON):**
```json
{
  "status": "queued",
  "run_id": "string",
  "estimated_completion": "2026-05-22T15:30:00Z"
}
```

### Usage Example (cURL)
```bash
curl -X POST https://your‑solar‑agent.com/api/run_simulation \
  -H "Content-Type: application/json" \
  -d '{"simulation_id":"demo","parameters":{"duration":120,"resolution":"medium","seed":42}}'
```

---
*This minimal artifact is intended for quick integration and testing of the SOLAR platform.*