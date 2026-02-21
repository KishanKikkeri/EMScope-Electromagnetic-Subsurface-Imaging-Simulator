"""
gui/main_window.py

Main application window for EMScope.
Connects simulation engine with visualization.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import numpy as np

from core.fdtd_solver import FDTDSolver
from core.material import layered_medium
from visualization.animation import animate_field
from visualization.plot_signal import plot_time_signal


class EMScopeApp:

    def __init__(self, root):
        self.root = root
        self.root.title("EMScope - Ground Penetrating Radar Simulator")
        self.root.geometry("600x400")

        self.create_widgets()

    # --------------------------------------------------
    # UI Layout
    # --------------------------------------------------

    def create_widgets(self):

        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Simulation Parameters",
                  font=("Arial", 14)).pack(pady=10)

        # Grid size
        ttk.Label(frame, text="Grid Size (nx):").pack()
        self.nx_entry = ttk.Entry(frame)
        self.nx_entry.insert(0, "400")
        self.nx_entry.pack()

        # Time steps
        ttk.Label(frame, text="Time Steps (nt):").pack()
        self.nt_entry = ttk.Entry(frame)
        self.nt_entry.insert(0, "800")
        self.nt_entry.pack()

        # Hidden object position
        ttk.Label(frame, text="Object Position Index:").pack()
        self.obj_pos_entry = ttk.Entry(frame)
        self.obj_pos_entry.insert(0, "250")
        self.obj_pos_entry.pack()

        # Object permittivity
        ttk.Label(frame, text="Object εr:").pack()
        self.obj_eps_entry = ttk.Entry(frame)
        self.obj_eps_entry.insert(0, "6.0")
        self.obj_eps_entry.pack()

        ttk.Button(frame,
                   text="Run Simulation",
                   command=self.run_simulation).pack(pady=20)

    # --------------------------------------------------
    # Simulation Runner
    # --------------------------------------------------

    def run_simulation(self):

        try:
            nx = int(self.nx_entry.get())
            nt = int(self.nt_entry.get())
            obj_pos = int(self.obj_pos_entry.get())
            obj_eps = float(self.obj_eps_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid input values.")
            return

        dx = 1e-3
        dt = dx / (3e8 * 2)

        # Build layered medium
        epsilon_r = layered_medium(
            nx,
            layers=[
                (0, 150, 1.0),   # Air
                (150, nx, 4.0)   # Soil
            ]
        )

        # Insert hidden object
        epsilon_r[obj_pos:obj_pos+10] = obj_eps

        solver = FDTDSolver(nx, dx, nt, dt, epsilon_r)

        solver.run()

        field_history = solver.field_history
        x = np.arange(nx) * dx

        animate_field(field_history, x)

        # Plot receiver signal (center of grid)
        receiver_index = 50
        signal = field_history[:, receiver_index]
        time = np.arange(nt) * dt

        plot_time_signal(time, signal,
                         title="Receiver Signal")

        messagebox.showinfo("Done",
                            "Simulation Completed Successfully!")


# --------------------------------------------------
# Launch App
# --------------------------------------------------

def launch():
    root = tk.Tk()
    app = EMScopeApp(root)
    root.mainloop()


if __name__ == "__main__":
    launch()
