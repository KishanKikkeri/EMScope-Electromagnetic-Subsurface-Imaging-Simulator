"""
gui/controls_panel.py

Handles all simulation input controls.
"""

import tkinter as tk
from tkinter import ttk


class ControlsPanel(ttk.Frame):

    def __init__(self, parent, run_callback):
        super().__init__(parent, padding=15)

        self.run_callback = run_callback

        self._build_ui()

    def _build_ui(self):

        ttk.Label(self,
                  text="Simulation Parameters",
                  font=("Arial", 14)).pack(pady=10)

        # Grid size
        ttk.Label(self, text="Grid Size (nx):").pack()
        self.nx = ttk.Entry(self)
        self.nx.insert(0, "400")
        self.nx.pack()

        # Time steps
        ttk.Label(self, text="Time Steps (nt):").pack()
        self.nt = ttk.Entry(self)
        self.nt.insert(0, "800")
        self.nt.pack()

        # Object position
        ttk.Label(self, text="Object Position:").pack()
        self.obj_pos = ttk.Entry(self)
        self.obj_pos.insert(0, "250")
        self.obj_pos.pack()

        # Object permittivity
        ttk.Label(self, text="Object εr:").pack()
        self.obj_eps = ttk.Entry(self)
        self.obj_eps.insert(0, "6.0")
        self.obj_eps.pack()

        ttk.Button(self,
                   text="Run Simulation",
                   command=self.run_callback).pack(pady=20)

    # --------------------------
    # Getter methods
    # --------------------------

    def get_values(self):
        return {
            "nx": int(self.nx.get()),
            "nt": int(self.nt.get()),
            "obj_pos": int(self.obj_pos.get()),
            "obj_eps": float(self.obj_eps.get())
        }
