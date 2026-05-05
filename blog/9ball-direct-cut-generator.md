# 9‑Ball AI Direct Cut Shot Candidate Generator

This minimal automation artifact provides a simple Python function to generate candidate cut shots for a 9‑ball pool AI.

```python
import math
from typing import List, Tuple

def generate_direct_cut_candidates(ball_positions: List[Tuple[float, float]], target_ball_index: int, cue_ball_index: int = 0) -> List[Tuple[float, float]]:
    """Generate candidate aim points for a direct cut shot.

    Args:
        ball_positions: List of (x, y) coordinates for all balls on the table.
        target_ball_index: Index in ball_positions of the ball to pocket.
        cue_ball_index: Index of the cue ball (default 0).

    Returns:
        List of (aim_x, aim_y) points on the cue ball where the tip should strike.
    """
    cue = ball_positions[cue_ball_index]
    target = ball_positions[target_ball_index]
    # Vector from cue to target
    dx, dy = target[0] - cue[0], target[1] - cue[1]
    distance = math.hypot(dx, dy)
    if distance == 0:
        return []
    # Normalized direction
    nx, ny = dx / distance, dy / distance
    # Offset by ball radius (≈ 0.05715 m) to hit the object ball's edge
    radius = 0.05715
    # Aim point is cue ball center minus offset along direction
    aim_x = cue[0] + (distance - radius) * nx
    aim_y = cue[1] + (distance - radius) * ny
    return [(aim_x, aim_y)]
```

You can import this function in your AI pipeline and feed it the current table state to obtain a concrete aim point for a direct cut shot.
