"""Position-time graph for physics/mechanics/average-velocity.

Regenerate after editing:
    python3 graphs/average_velocity.py
then commit the updated SVG along with the post.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# The two points the average velocity is taken between. Change these and
# rerun to move the secant line.
T1, T2 = 2.0, 8.0

OUT = (
    Path(__file__).parent.parent
    / "public/images/physics/mechanics/average-velocity/position-time.svg"
)

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 11,
})

# A messy but reproducible trajectory: smoothed random velocities,
# integrated to get position. Change the seed for a different wiggle.
rng = np.random.default_rng(7)
t = np.linspace(0, 10, 400)
v = 1.5 + rng.normal(0.0, 4.0, t.size)
v = np.convolve(v, np.ones(25) / 25, mode="same")
x = np.concatenate([[0.0], np.cumsum(v[:-1] * np.diff(t))])

x1, x2 = np.interp([T1, T2], t, x)
v_avg = (x2 - x1) / (T2 - T1)

fig, ax = plt.subplots(figsize=(6.4, 4.0))
ax.plot(t, x, color="#1155cc", linewidth=1.8, label="position $x(t)$")
ax.plot(
    [T1, T2], [x1, x2],
    color="#c0392b", linewidth=1.8, linestyle="--",
    label=rf"secant: $\bar{{v}} = {v_avg:.2f}$ m/s",
)
ax.plot([T1, T2], [x1, x2], "o", color="#c0392b", zorder=3)
ax.annotate("$(t_1, x_1)$", (T1, x1), textcoords="offset points", xytext=(8, -14))
ax.annotate("$(t_2, x_2)$", (T2, x2), textcoords="offset points", xytext=(8, -14))

ax.set_xlabel("$t$ (s)")
ax.set_ylabel("$x$ (m)")
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False)
fig.tight_layout()

OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT)
print(f"wrote {OUT}")
