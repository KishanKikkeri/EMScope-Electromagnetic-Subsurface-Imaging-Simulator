"""
physics/constants.py

Physical constants used throughout the EMScope simulation.
All values are in SI units.
"""

import numpy as np

# Speed of light in vacuum (m/s)
C0 = 299_792_458  

# Vacuum permittivity (F/m)
EPSILON_0 = 8.854187817e-12  

# Vacuum permeability (H/m)
MU_0 = 4 * np.pi * 1e-7  

# Free-space impedance (Ohms)
Z0 = np.sqrt(MU_0 / EPSILON_0)
