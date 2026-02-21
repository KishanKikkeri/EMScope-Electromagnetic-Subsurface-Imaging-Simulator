"""
visualization/animation.py

Animation utilities for EM wave propagation.
Displays real-time evolution of electric field.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# -------------------------------------------------------
# Animate Electric Field Evolution
# -------------------------------------------------------

def animate_field(field_history, x, interval=30,
                  title="EM Wave Propagation"):
    """
    Animate electric field over time.

    Parameters
    ----------
    field_history : ndarray (nt, nx)
        Time history of Ez field
    x : ndarray
        Spatial coordinates
    interval : int
        Delay between frames (ms)
    """

    nt, nx = field_history.shape

    fig, ax = plt.subplots()
    line, = ax.plot(x, field_history[0])

    ax.set_xlabel("Position (m)")
    ax.set_ylabel("Electric Field (Ez)")
    ax.set_title(title)
    ax.grid(True)

    def update(frame):
        line.set_ydata(field_history[frame])
        ax.set_title(f"{title} | Time Step: {frame}")
        return line,

    ani = FuncAnimation(
        fig,
        update,
        frames=nt,
        interval=interval,
        blit=True
    )

    plt.tight_layout()
    plt.show()

    return ani


# -------------------------------------------------------
# Animate with Material Overlay
# -------------------------------------------------------

def animate_field_with_material(field_history,
                                x,
                                epsilon_r,
                                interval=30):
    """
    Animate field with material profile overlay.
    """

    nt, nx = field_history.shape

    fig, ax1 = plt.subplots()

    line, = ax1.plot(x, field_history[0])
    ax1.set_xlabel("Position (m)")
    ax1.set_ylabel("Electric Field (Ez)")
    ax1.grid(True)

    ax2 = ax1.twinx()
    ax2.plot(x, epsilon_r, linestyle="--")
    ax2.set_ylabel("Relative Permittivity (εr)")

    def update(frame):
        line.set_ydata(field_history[frame])
        ax1.set_title(f"Wave Propagation | Step: {frame}")
        return line,

    ani = FuncAnimation(
        fig,
        update,
        frames=nt,
        interval=interval,
        blit=True
    )

    plt.tight_layout()
    plt.show()

    return ani
