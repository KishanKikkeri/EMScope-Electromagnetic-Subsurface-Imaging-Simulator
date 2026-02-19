"""
physics/reflection.py

Analytical reflection and transmission calculations
for EM waves at material boundaries.
"""

import numpy as np


# -----------------------------------------------------
# Intrinsic Impedance
# -----------------------------------------------------

def intrinsic_impedance(mu, epsilon):
    """
    Compute intrinsic impedance of a medium.

    Z = sqrt(mu / epsilon)

    Parameters
    ----------
    mu : float
        Absolute permeability (H/m)
    epsilon : float
        Absolute permittivity (F/m)

    Returns
    -------
    float
        Intrinsic impedance (Ohms)
    """
    if mu <= 0 or epsilon <= 0:
        raise ValueError("mu and epsilon must be positive.")

    return np.sqrt(mu / epsilon)


# -----------------------------------------------------
# Reflection Coefficient (Amplitude)
# -----------------------------------------------------

def reflection_coefficient(Z1, Z2):
    """
    Compute amplitude reflection coefficient.

    Γ = (Z2 - Z1) / (Z2 + Z1)

    Parameters
    ----------
    Z1 : float
        Impedance of medium 1
    Z2 : float
        Impedance of medium 2

    Returns
    -------
    float
        Reflection coefficient (amplitude)
    """
    if (Z1 + Z2) == 0:
        raise ValueError("Invalid impedance values.")

    return (Z2 - Z1) / (Z2 + Z1)


# -----------------------------------------------------
# Transmission Coefficient (Amplitude)
# -----------------------------------------------------

def transmission_coefficient(Z1, Z2):
    """
    Compute amplitude transmission coefficient.

    T = 2Z2 / (Z2 + Z1)

    Parameters
    ----------
    Z1 : float
        Impedance of medium 1
    Z2 : float
        Impedance of medium 2

    Returns
    -------
    float
        Transmission coefficient (amplitude)
    """
    if (Z1 + Z2) == 0:
        raise ValueError("Invalid impedance values.")

    return (2 * Z2) / (Z2 + Z1)


# -----------------------------------------------------
# Power Reflection Coefficient
# -----------------------------------------------------

def power_reflection_coefficient(Z1, Z2):
    """
    Power reflection coefficient.

    R = |Γ|^2
    """
    gamma = reflection_coefficient(Z1, Z2)
    return abs(gamma) ** 2


# -----------------------------------------------------
# Power Transmission Coefficient
# -----------------------------------------------------

def power_transmission_coefficient(Z1, Z2):
    """
    Power transmission coefficient.

    T_power = 1 - R
    """
    R = power_reflection_coefficient(Z1, Z2)
    return 1 - R
