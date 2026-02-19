"""
signal_processing/depth_estimation.py

Depth estimation utilities for subsurface object detection
using time-of-flight analysis.
"""

import numpy as np
from physics.constants import C0


# -------------------------------------------------------
# Index to Time Conversion
# -------------------------------------------------------

def index_to_time(index, dt):
    """
    Convert signal index to time.

    Parameters
    ----------
    index : int
    dt : float

    Returns
    -------
    float
        Time in seconds
    """
    return index * dt


# -------------------------------------------------------
# Wave Velocity in Medium
# -------------------------------------------------------

def wave_velocity(epsilon_r, mu_r=1.0):
    """
    Compute wave velocity in material.

    v = c / sqrt(epsilon_r * mu_r)
    """
    if epsilon_r <= 0 or mu_r <= 0:
        raise ValueError("Material parameters must be positive.")

    return C0 / np.sqrt(epsilon_r * mu_r)


# -------------------------------------------------------
# Depth from Time-of-Flight
# -------------------------------------------------------

def estimate_depth(time_of_flight, epsilon_r, mu_r=1.0):
    """
    Estimate object depth assuming homogeneous medium.

    Uses two-way travel time.

    d = (v * t) / 2
    """

    v = wave_velocity(epsilon_r, mu_r)

    return (v * time_of_flight) / 2


# -------------------------------------------------------
# Depth from Index Directly
# -------------------------------------------------------

def estimate_depth_from_index(index, dt, epsilon_r, mu_r=1.0):
    """
    Full pipeline:
    index -> time -> depth
    """

    t = index_to_time(index, dt)
    return estimate_depth(t, epsilon_r, mu_r)


# -------------------------------------------------------
# Multiple Peak Depth Estimation
# -------------------------------------------------------

def estimate_multiple_depths(peak_indices, dt, epsilon_r, mu_r=1.0):
    """
    Estimate depths for multiple detected peaks.

    Returns
    -------
    list of depths
    """

    depths = []

    for idx in peak_indices:
        depth = estimate_depth_from_index(idx, dt, epsilon_r, mu_r)
        depths.append(depth)

    return depths
