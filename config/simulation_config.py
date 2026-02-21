"""
config/simulation_config.py

Simulation presets and radar configurations.
"""

# --------------------------------------------------
# Grid Presets
# --------------------------------------------------

GRID_PRESETS = {
    "Small Test": {
        "nx": 200,
        "nt": 400,
        "dx": 1e-3
    },
    "Standard GPR": {
        "nx": 400,
        "nt": 800,
        "dx": 1e-3
    },
    "High Resolution": {
        "nx": 800,
        "nt": 1500,
        "dx": 5e-4
    }
}

# --------------------------------------------------
# Radar Frequency Presets (Hz)
# --------------------------------------------------

RADAR_FREQUENCIES = {
    "Low Frequency (50 MHz)": 50e6,
    "Medium Frequency (250 MHz)": 250e6,
    "High Frequency (1 GHz)": 1e9
}

# --------------------------------------------------
# CFL Stability Safety Factor
# --------------------------------------------------

CFL_SAFETY_FACTOR = 0.99

# --------------------------------------------------
# Predefined Layered Profiles
# --------------------------------------------------

LAYER_PROFILES = {

    "Air-Soil": [
        (0, 150, "Air"),
        (150, 400, "Dry Soil")
    ],

    "Air-MoistSoil": [
        (0, 150, "Air"),
        (150, 400, "Moist Soil")
    ],

    "Air-Concrete": [
        (0, 100, "Air"),
        (100, 400, "Concrete")
    ],

    "Road Structure": [
        (0, 80, "Air"),
        (80, 200, "Asphalt"),
        (200, 400, "Dry Soil")
    ]
}
