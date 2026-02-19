"""
core/boundary.py

Boundary condition implementations for FDTD simulation.
Supports simple absorbing boundary conditions (ABC).
"""

import numpy as np


class BoundaryCondition:
    """
    Base class for boundary conditions.
    """

    def apply(self, Ez):
        """
        Apply boundary condition to electric field array.

        Parameters
        ----------
        Ez : ndarray
            Electric field array
        """
        raise NotImplementedError("Boundary condition must implement apply().")


# -------------------------------------------------------
# First-Order Absorbing Boundary Condition (ABC)
# -------------------------------------------------------

class FirstOrderABC(BoundaryCondition):
    """
    Simple first-order absorbing boundary condition.

    E(0) = E(1)
    E(N-1) = E(N-2)
    """

    def apply(self, Ez):
        Ez[0] = Ez[1]
        Ez[-1] = Ez[-2]


# -------------------------------------------------------
# Perfect Electric Conductor (PEC)
# -------------------------------------------------------

class PECBoundary(BoundaryCondition):
    """
    Perfect Electric Conductor boundary condition.

    Forces electric field to zero at boundaries.
    """

    def apply(self, Ez):
        Ez[0] = 0.0
        Ez[-1] = 0.0
