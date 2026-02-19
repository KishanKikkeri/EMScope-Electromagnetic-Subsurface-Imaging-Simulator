"""
signal_processing/peak_detection.py

Peak detection utilities for reflected EM signals.
Used for identifying reflection events from layers
and concealed objects.
"""

import numpy as np


# -------------------------------------------------------
# Basic Peak Detection
# -------------------------------------------------------

def detect_peaks(signal, threshold_ratio=0.2):
    """
    Detect local maxima above threshold.

    Parameters
    ----------
    signal : ndarray
        Reflected signal array
    threshold_ratio : float
        Fraction of max amplitude to define threshold

    Returns
    -------
    list
        Indices of detected peaks
    """

    if len(signal) < 3:
        return []

    threshold = threshold_ratio * np.max(np.abs(signal))
    peaks = []

    for i in range(1, len(signal) - 1):
        if (
            abs(signal[i]) > threshold
            and abs(signal[i]) > abs(signal[i - 1])
            and abs(signal[i]) > abs(signal[i + 1])
        ):
            peaks.append(i)

    return peaks


# -------------------------------------------------------
# Peak Detection with Minimum Distance
# -------------------------------------------------------

def detect_peaks_with_distance(signal, threshold_ratio=0.2, min_distance=10):
    """
    Detect peaks while enforcing minimum separation.

    Parameters
    ----------
    signal : ndarray
    threshold_ratio : float
    min_distance : int
        Minimum index spacing between peaks

    Returns
    -------
    list
        Peak indices
    """

    candidate_peaks = detect_peaks(signal, threshold_ratio)

    if not candidate_peaks:
        return []

    filtered_peaks = [candidate_peaks[0]]

    for idx in candidate_peaks[1:]:
        if idx - filtered_peaks[-1] >= min_distance:
            filtered_peaks.append(idx)

    return filtered_peaks


# -------------------------------------------------------
# Peak Amplitudes
# -------------------------------------------------------

def peak_amplitudes(signal, peak_indices):
    """
    Extract amplitudes at detected peaks.

    Parameters
    ----------
    signal : ndarray
    peak_indices : list

    Returns
    -------
    list
        Peak amplitudes
    """

    return [signal[i] for i in peak_indices]


# -------------------------------------------------------
# Signal Energy
# -------------------------------------------------------

def signal_energy(signal):
    """
    Compute total signal energy.

    E = sum(signal^2)
    """

    return np.sum(signal ** 2)
