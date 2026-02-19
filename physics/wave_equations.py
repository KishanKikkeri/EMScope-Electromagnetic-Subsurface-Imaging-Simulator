"""
physics/wave_equations.py

Utility functions for FDTD wave propagation.
Includes Courant stability condition and update coefficient calculations.
"""

import numpy as np
from physics.constants import C0, EPSILON_0, MU_0


def compute_time_step(dx, courant_factor=0.99):
    """
    Compute stable time step using Courant condition for 1D FDTD.

    Parameters:
        dx (float): Spatial step size (meters)
        courant_factor (float): Stability scaling factor (< 1)

    Returns:
        dt (float): Stable time step (seconds)
    """
    if dx <= 0:
        raise ValueError("Spatial step dx must be positive.")

    dt = courant_factor * dx / C0
    return dt


def compute_update_coefficients(epsilon_r, sigma, dt, dx):
    """
    Compute FDTD update coefficients for electric field in lossy medium.

    Parameters:
        epsilon_r (ndarray): Relative permittivity array
        sigma (ndarray): Conductivity array (S/m)
        dt (float): Time step
        dx (float): Spatial step

    Returns:
        Ceze, Cezh: Coefficient arrays for E-field update
    """
    if dt <= 0 or dx <= 0:
        raise ValueError("dt and dx must be positive.")

    epsilon = EPSILON_0 * epsilon_r

    Ceze = (1 - (sigma * dt) / (2 * epsilon)) / (1 + (sigma * dt) / (2 * epsilon))
    Cezh = (dt / (epsilon * dx)) / (1 + (sigma * dt) / (2 * epsilon))

    return Ceze, Cezh


def compute_magnetic_coefficient(dt, dx):
    """
    Compute magnetic field update coefficient (lossless medium assumed).

    Parameters:
        dt (float): Time step
        dx (float): Spatial step

    Returns:
        Chye (float): Magnetic field update coefficient
    """
    if dt <= 0 or dx <= 0:
        raise ValueError("dt and dx must be positive.")

    Chye = dt / (MU_0 * dx)
    return Chye
