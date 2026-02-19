"""
core/grid.py

Defines 1D spatial grid and material assignment
for layered subsurface simulations.
"""

import numpy as np
from core.material import Material


class Grid1D:
    """
    1D spatial grid for EM wave propagation.

    Attributes
    ----------
    nx : int
        Number of spatial points.
    dx : float
        Spatial resolution (meters).
    x : ndarray
        Spatial coordinates.
    epsilon_r : ndarray
        Relative permittivity distribution.
    sigma : ndarray
        Conductivity distribution.
    """

    def __init__(self, nx, dx, background_material=None):
        if nx <= 0:
            raise ValueError("nx must be positive.")
        if dx <= 0:
            raise ValueError("dx must be positive.")

        self.nx = nx
        self.dx = dx
        self.x = np.linspace(0, (nx - 1) * dx, nx)

        # Default background = free space
        if background_material is None:
            background_material = Material("Free Space", 1.0, 1.0, 0.0)

        self.background_material = background_material

        # Material arrays
        self.epsilon_r = np.full(nx, background_material.epsilon_r)
        self.sigma = np.full(nx, background_material.sigma)

    # --------------------------------------------------
    # Layer Assignment
    # --------------------------------------------------

    def add_layer(self, start, end, material):
        """
        Assign a material layer between spatial positions.

        Parameters
        ----------
        start : float
            Start position (meters)
        end : float
            End position (meters)
        material : Material
            Material object
        """
        if not isinstance(material, Material):
            raise TypeError("material must be a Material object.")

        if start < 0 or end > self.x[-1] or start >= end:
            raise ValueError("Invalid layer boundaries.")

        indices = np.where((self.x >= start) & (self.x <= end))

        self.epsilon_r[indices] = material.epsilon_r
        self.sigma[indices] = material.sigma

    # --------------------------------------------------
    # Object Embedding
    # --------------------------------------------------

    def embed_object(self, center, width, material):
        """
        Embed hidden object in the medium.

        Parameters
        ----------
        center : float
            Object center position (meters)
        width : float
            Object width (meters)
        material : Material
            Material object
        """
        if not isinstance(material, Material):
            raise TypeError("material must be a Material object.")

        if width <= 0:
            raise ValueError("width must be positive.")

        start = center - width / 2
        end = center + width / 2

        if start < 0 or end > self.x[-1]:
            raise ValueError("Object exceeds grid boundaries.")

        indices = np.where((self.x >= start) & (self.x <= end))

        self.epsilon_r[indices] = material.epsilon_r
        self.sigma[indices] = material.sigma

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def reset_medium(self):
        """
        Reset entire grid to background material.
        """
        self.epsilon_r[:] = self.background_material.epsilon_r
        self.sigma[:] = self.background_material.sigma
