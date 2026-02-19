"""
core/fdtd_solver.py

1D FDTD solver for EM wave propagation in layered media.
Implements Yee algorithm for Ez-Hy fields.
"""

import numpy as np
from physics.wave_equations import (
    compute_update_coefficients,
    compute_magnetic_coefficient
)


class FDTDSolver1D:
    """
    1D FDTD solver (Ez-Hy mode).
    """

    def __init__(self, grid, dt, total_time, source_position):
        if source_position < 0 or source_position >= grid.nx:
            raise ValueError("Invalid source position index.")

        self.grid = grid
        self.dt = dt
        self.total_time = total_time
        self.source_position = source_position

        self.nt = int(total_time / dt)

        # Field arrays
        self.Ez = np.zeros(grid.nx)
        self.Hy = np.zeros(grid.nx - 1)

        # Reflection recording (at source location)
        self.reflected_signal = np.zeros(self.nt)

        # Precompute update coefficients
        self.Ceze, self.Cezh = compute_update_coefficients(
            grid.epsilon_r,
            grid.sigma,
            dt,
            grid.dx
        )

        self.Chye = compute_magnetic_coefficient(dt, grid.dx)

    def run(self, source_signal):
        """
        Run FDTD simulation.

        Parameters:
            source_signal (ndarray): Time-domain source array
        """
        if len(source_signal) != self.nt:
            raise ValueError("Source signal length mismatch.")

        for n in range(self.nt):

            # --- Update Magnetic Field ---
            for i in range(self.grid.nx - 1):
                self.Hy[i] += self.Chye * (
                    self.Ez[i + 1] - self.Ez[i]
                )

            # --- Update Electric Field ---
            for i in range(1, self.grid.nx - 1):
                self.Ez[i] = (
                    self.Ceze[i] * self.Ez[i]
                    + self.Cezh[i] * (self.Hy[i] - self.Hy[i - 1])
                )

            # --- Source Injection (Soft Source) ---
            self.Ez[self.source_position] += source_signal[n]

            # --- Simple Absorbing Boundary (1st order ABC) ---
            self.Ez[0] = self.Ez[1]
            self.Ez[-1] = self.Ez[-2]

            # --- Record Reflection ---
            self.reflected_signal[n] = self.Ez[self.source_position]

        return self.reflected_signal
