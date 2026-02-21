"""
visualization/plot_signal.py

Signal plotting utilities for EMScope.
Used to visualize reflected EM signals and detected peaks.
"""

import numpy as np
import matplotlib.pyplot as plt


# -------------------------------------------------------
# Plot Reflected Signal
# -------------------------------------------------------

def plot_signal(signal, dt, title="Reflected Signal"):
    """
    Plot time-domain reflected signal.

    Parameters
    ----------
    signal : ndarray
    dt : float
    title : str
    """

    time = np.arange(len(signal)) * dt

    plt.figure()
    plt.plot(time, signal)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# -------------------------------------------------------
# Plot Signal with Peaks
# -------------------------------------------------------

def plot_signal_with_peaks(signal, dt, peak_indices,
                           title="Reflected Signal with Peaks"):
    """
    Plot signal and highlight detected peaks.
    """

    time = np.arange(len(signal)) * dt
    peak_times = [i * dt for i in peak_indices]
    peak_values = [signal[i] for i in peak_indices]

    plt.figure()
    plt.plot(time, signal, label="Signal")
    plt.scatter(peak_times, peak_values, marker='o', label="Detected Peaks")

    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# -------------------------------------------------------
# Plot Signal Comparison
# -------------------------------------------------------

def plot_comparison(clean_signal, noisy_signal, dt):
    """
    Compare clean vs noisy signals.
    """

    time = np.arange(len(clean_signal)) * dt

    plt.figure()
    plt.plot(time, clean_signal, label="Clean Signal")
    plt.plot(time, noisy_signal, label="Noisy Signal", linestyle="--")

    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Signal Comparison")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
