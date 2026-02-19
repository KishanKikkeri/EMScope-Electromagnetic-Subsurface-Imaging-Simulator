"""
physics/attenuation.py

Attenuation and propagation calculations
for EM waves in lossy media.
"""

import numpy as np
from physics.constants import EPSILON_0, MU_0


# -------------------------------------------------------
# Complex Propagation Constant
# -------------------------------------------------------

def propagation_constant(frequency, epsilon_r, mu_r=1.0, sigma=0.0):
    """
    Compute complex propagation constant gamma.

    gamma = alpha + j*beta

    Parameters
    ----------
    frequency : float
        Frequency (Hz)
    epsilon_r : float
        Relative permittivity
    mu_r : float
        Relative permeability
    sigma : float
        Conductivity (S/m)

    Returns
    -------
    gamma : complex
        Complex propagation constant
    """

    if frequency <= 0:
        raise ValueError("Frequency must be positive.")

    omega = 2 * np.pi * frequency
    epsilon = EPSILON_0 * epsilon_r
    mu = MU_0 * mu_r

    gamma = np.sqrt(1j * omega * mu * (sigma + 1j * omega * epsilon))

    return gamma


# -------------------------------------------------------
# Attenuation Constant (alpha)
# -------------------------------------------------------

def attenuation_constant(frequency, epsilon_r, mu_r=1.0, sigma=0.0):
    """
    Extract attenuation constant alpha (Np/m).
    """
    gamma = propagation_constant(frequency, epsilon_r, mu_r, sigma)
    return np.real(gamma)


# -------------------------------------------------------
# Phase Constant (beta)
# -------------------------------------------------------

def phase_constant(frequency, epsilon_r, mu_r=1.0, sigma=0.0):
    """
    Extract phase constant beta (rad/m).
    """
    gamma = propagation_constant(frequency, epsilon_r, mu_r, sigma)
    return np.imag(gamma)


# -------------------------------------------------------
# Skin Depth
# -------------------------------------------------------

def skin_depth(frequency, epsilon_r, mu_r=1.0, sigma=0.0):
    """
    Compute skin depth.

    delta = 1 / alpha
    """
    alpha = attenuation_constant(frequency, epsilon_r, mu_r, sigma)

    if alpha == 0:
        return np.inf

    return 1 / alpha


# -------------------------------------------------------
# Good Conductor Approximation
# -------------------------------------------------------

def good_conductor_attenuation(frequency, sigma, mu_r=1.0):
    """
    Approximate attenuation for good conductor.

    alpha ≈ sqrt(pi * f * mu * sigma)
    """
    if frequency <= 0:
        raise ValueError("Frequency must be positive.")

    mu = MU_0 * mu_r
    return np.sqrt(np.pi * frequency * mu * sigma)
