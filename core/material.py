"""
core/material.py

Material definitions for EM simulation.
Encapsulates electromagnetic properties of media.
"""

import numpy as np
from physics.constants import EPSILON_0, MU_0


class Material:
    """
    Represents an electromagnetic material.

    Parameters
    ----------
    name : str
        Name of the material.
    epsilon_r : float
        Relative permittivity.
    mu_r : float
        Relative permeability.
    sigma : float
        Electrical conductivity (S/m).
    """

    def __init__(self, name, epsilon_r=1.0, mu_r=1.0, sigma=0.0):
        if epsilon_r <= 0:
            raise ValueError("epsilon_r must be positive.")
        if mu_r <= 0:
            raise ValueError("mu_r must be positive.")
        if sigma < 0:
            raise ValueError("sigma cannot be negative.")

        self.name = name
        self.epsilon_r = epsilon_r
        self.mu_r = mu_r
        self.sigma = sigma

    @property
    def epsilon(self):
        """Absolute permittivity (F/m)."""
        return EPSILON_0 * self.epsilon_r

    @property
    def mu(self):
        """Absolute permeability (H/m)."""
        return MU_0 * self.mu_r

    @property
    def wave_velocity(self):
        """
        Wave propagation velocity in material (m/s).
        v = 1 / sqrt(mu * epsilon)
        """
        return 1.0 / np.sqrt(self.mu * self.epsilon)

    @property
    def impedance(self):
        """
        Intrinsic impedance of material (Ohms).
        Z = sqrt(mu / epsilon)
        """
        return np.sqrt(self.mu / self.epsilon)

    def to_dict(self):
        """Return material properties as dictionary."""
        return {
            "name": self.name,
            "epsilon_r": self.epsilon_r,
            "mu_r": self.mu_r,
            "sigma": self.sigma
        }

    def __repr__(self):
        return (
            f"Material(name={self.name}, "
            f"epsilon_r={self.epsilon_r}, "
            f"mu_r={self.mu_r}, "
            f"sigma={self.sigma})"
        )
