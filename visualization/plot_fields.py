"""
visualization/plot_fields.py

Field visualization utilities for EMScope.
Used to display spatial EM field snapshots
and material distributions.
"""

import numpy as np
import matplotlib.pyplot as plt


# -------------------------------------------------------
# Plot Electric Field Snapshot
# -------------------------------------------------------

def plot_electric_field(Ez, x, title="Electric Field Snapshot"):
    """
    Plot spatial electric field distribution.

    Parameters
    ----------
    Ez : ndarray
        Electric field array
    x : ndarray
        Spatial coordinates
    """

    plt.figure()
    plt.plot(x, Ez)
    plt.xlabel("Position (m)")
    plt.ylabel("Electric Field (Ez)")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# -------------------------------------------------------
# Plot Material Profile
# -------------------------------------------------------

def plot_material_profile(x, epsilon_r, sigma=None):
    """
    Plot material permittivity (and optionally conductivity).

    Parameters
    ----------
    x : ndarray
    epsilon_r : ndarray
    sigma : ndarray (optional)
    """

    plt.figure()

    plt.plot(x, epsilon_r, label="Relative Permittivity (εr)")

    if sigma is not None:
        plt.plot(x, sigma, linestyle="--", label="Conductivity (σ)")

    plt.xlabel("Position (m)")
    plt.ylabel("Material Properties")
    plt.title("Material Distribution")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# -------------------------------------------------------
# Combined Field + Material View
# -------------------------------------------------------

def plot_field_with_material(Ez, x, epsilon_r):
    """
    Plot electric field and material profile together.
    """

    fig, ax1 = plt.subplots()

    ax1.plot(x, Ez)
    ax1.set_xlabel("Position (m)")
    ax1.set_ylabel("Electric Field (Ez)")
    ax1.grid(True)

    ax2 = ax1.twinx()
    ax2.plot(x, epsilon_r, linestyle="--")
    ax2.set_ylabel("Relative Permittivity (εr)")

    plt.title("Field and Material Profile")
    fig.tight_layout()
    plt.show()
