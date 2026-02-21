"""
gui/results_panel.py

Handles simulation output display.
"""

import numpy as np
from tkinter import ttk

from visualization.animation import animate_field
from visualization.plot_signal import plot_time_signal


class ResultsPanel(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent, padding=15)

        ttk.Label(self,
                  text="Simulation Results",
                  font=("Arial", 14)).pack(pady=10)

    # --------------------------------------------------

    def display_results(self, solver):

        field_history = solver.field_history
        nx = solver.nx
        dx = solver.dx
        nt = solver.nt
        dt = solver.dt

        x = np.arange(nx) * dx

        animate_field(field_history, x)

        # Receiver at index 50
        receiver_index = 50
        signal = field_history[:, receiver_index]
        time = np.arange(nt) * dt

        plot_time_signal(time, signal,
                         title="Receiver Signal")
