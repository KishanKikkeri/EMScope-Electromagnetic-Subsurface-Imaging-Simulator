"""
config/material_database.py

Extended electromagnetic material database
for subsurface sensing simulations.
"""

MATERIAL_DATABASE = {

    # -----------------------------------------
    # Atmospheric
    # -----------------------------------------
    "Air": {
        "epsilon_r": 1.0006,
        "sigma": 0.0,
        "mu_r": 1.0,
        "category": "atmospheric"
    },

    # -----------------------------------------
    # Soil Types
    # -----------------------------------------
    "Dry Soil": {
        "epsilon_r": 3.0,
        "sigma": 0.001,
        "mu_r": 1.0,
        "category": "soil"
    },

    "Moist Soil": {
        "epsilon_r": 10.0,
        "sigma": 0.02,
        "mu_r": 1.0,
        "category": "soil"
    },

    "Wet Soil": {
        "epsilon_r": 20.0,
        "sigma": 0.1,
        "mu_r": 1.0,
        "category": "soil"
    },

    "Dry Sand": {
        "epsilon_r": 2.5,
        "sigma": 0.0001,
        "mu_r": 1.0,
        "category": "soil"
    },

    "Clay": {
        "epsilon_r": 15.0,
        "sigma": 0.5,
        "mu_r": 1.0,
        "category": "soil"
    },

    # -----------------------------------------
    # Liquids
    # -----------------------------------------
    "Fresh Water": {
        "epsilon_r": 80.0,
        "sigma": 0.01,
        "mu_r": 1.0,
        "category": "liquid"
    },

    "Sea Water": {
        "epsilon_r": 80.0,
        "sigma": 4.0,
        "mu_r": 1.0,
        "category": "liquid"
    },

    # -----------------------------------------
    # Construction Materials
    # -----------------------------------------
    "Concrete": {
        "epsilon_r": 6.0,
        "sigma": 0.01,
        "mu_r": 1.0,
        "category": "construction"
    },

    "Asphalt": {
        "epsilon_r": 5.0,
        "sigma": 0.02,
        "mu_r": 1.0,
        "category": "construction"
    },

    "Brick": {
        "epsilon_r": 4.5,
        "sigma": 0.02,
        "mu_r": 1.0,
        "category": "construction"
    },

    # -----------------------------------------
    # Metals (idealized)
    # -----------------------------------------
    "Aluminum": {
        "epsilon_r": 1.0,
        "sigma": 3.5e7,
        "mu_r": 1.0,
        "category": "metal"
    },

    "Copper": {
        "epsilon_r": 1.0,
        "sigma": 5.8e7,
        "mu_r": 1.0,
        "category": "metal"
    },

    "Steel": {
        "epsilon_r": 1.0,
        "sigma": 1e6,
        "mu_r": 100.0,
        "category": "metal"
    }
}
