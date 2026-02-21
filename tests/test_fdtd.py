"""
tests/test_fdtd.py
"""

import numpy as np
from core.fdtd_solver import FDTDSolver


def test_solver_runs():
    nx = 100
    dx = 1e-3
    nt = 100
    dt = dx / (3e8 * 2)

    epsilon_r = np.ones(nx)

    solver = FDTDSolver(nx, dx, nt, dt, epsilon_r)
    solver.run()

    assert solver.field_history.shape == (nt, nx)
