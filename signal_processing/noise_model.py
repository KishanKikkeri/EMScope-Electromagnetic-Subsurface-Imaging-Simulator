"""
signal_processing/noise_model.py

Noise modeling utilities for EM signal simulation.
Adds realistic disturbances to reflected signals.
"""

import numpy as np


# -------------------------------------------------------
# Additive White Gaussian Noise (AWGN)
# -------------------------------------------------------

def add_awgn(signal, snr_db):
    """
    Add additive white Gaussian noise to signal.

    Parameters
    ----------
    signal : ndarray
    snr_db : float
        Signal-to-noise ratio in dB

    Returns
    -------
    ndarray
        Noisy signal
    """

    if snr_db <= 0:
        raise ValueError("SNR must be positive.")

    signal_power = np.mean(signal ** 2)

    snr_linear = 10 ** (snr_db / 10)

    noise_power = signal_power / snr_linear

    noise = np.random.normal(
        0,
        np.sqrt(noise_power),
        size=signal.shape
    )

    return signal + noise


# -------------------------------------------------------
# Impulse Noise
# -------------------------------------------------------

def add_impulse_noise(signal, probability=0.01, amplitude_factor=2.0):
    """
    Add random impulse spikes to signal.

    Parameters
    ----------
    probability : float
        Probability of impulse occurrence
    amplitude_factor : float
        Multiplier relative to max signal amplitude
    """

    noisy_signal = signal.copy()
    max_amp = np.max(np.abs(signal))

    for i in range(len(signal)):
        if np.random.rand() < probability:
            spike = amplitude_factor * max_amp
            noisy_signal[i] += spike * np.random.choice([-1, 1])

    return noisy_signal


# -------------------------------------------------------
# Multipath Distortion (Simple Model)
# -------------------------------------------------------

def add_multipath(signal, delay_samples=20, attenuation=0.3):
    """
    Simulate simple multipath reflection.

    Adds delayed and attenuated copy of signal.
    """

    delayed_signal = np.zeros_like(signal)

    if delay_samples < len(signal):
        delayed_signal[delay_samples:] = signal[:-delay_samples]

    return signal + attenuation * delayed_signal


# -------------------------------------------------------
# Combined Noise Model
# -------------------------------------------------------

def apply_realistic_noise(signal,
                          snr_db=20,
                          impulse_prob=0.005,
                          multipath_delay=15,
                          multipath_attenuation=0.2):
    """
    Apply combined noise effects.

    Returns
    -------
    ndarray
        Distorted signal
    """

    noisy = add_awgn(signal, snr_db)
    noisy = add_impulse_noise(noisy, impulse_prob)
    noisy = add_multipath(noisy,
                          delay_samples=multipath_delay,
                          attenuation=multipath_attenuation)

    return noisy
