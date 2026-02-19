"""
core/source.py

Defines time-domain EM sources for FDTD simulation.
Includes Gaussian pulse and Ricker wavelet.
"""

import numpy as np


class Source:
    """
    Time-domain EM source generator.
    """

    def __init__(self, dt, total_time):
        if dt <= 0:
            raise ValueError("dt must be positive.")
        if total_time <= 0:
            raise ValueError("total_time must be positive.")

        self.dt = dt
        self.total_time = total_time
        self.time = np.arange(0, total_time, dt)

    def gaussian_pulse(self, t0, spread, amplitude=1.0):
        """
        Generate Gaussian pulse.

        Parameters:
            t0 (float): Pulse center time
            spread (float): Pulse width parameter
            amplitude (float): Peak amplitude

        Returns:
            ndarray: Gaussian pulse signal
        """
        return amplitude * np.exp(-((self.time - t0) ** 2) / (2 * spread ** 2))

    def ricker_wavelet(self, f0, amplitude=1.0):
        """
        Generate Ricker wavelet (GPR standard source).

        Parameters:
            f0 (float): Central frequency (Hz)
            amplitude (float): Peak amplitude

        Returns:
            ndarray: Ricker wavelet signal
        """
        if f0 <= 0:
            raise ValueError("Central frequency must be positive.")

        t = self.time - 1.5 / f0
        term = (np.pi * f0 * t) ** 2
        return amplitude * (1 - 2 * term) * np.exp(-term)

    def sine_wave(self, frequency, amplitude=1.0):
        """
        Generate continuous sine wave.

        Parameters:
            frequency (float): Frequency in Hz
            amplitude (float): Peak amplitude

        Returns:
            ndarray: Sine wave signal
        """
        if frequency <= 0:
            raise ValueError("Frequency must be positive.")

        return amplitude * np.sin(2 * np.pi * frequency * self.time)
