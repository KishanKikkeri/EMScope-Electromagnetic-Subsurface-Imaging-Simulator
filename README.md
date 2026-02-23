# EMScope

EMScope is a GUI-based electromagnetic (EM) wave simulation and subsurface sensing tool designed to model wave propagation in layered media and detect hidden objects using reflected signal analysis.

The system simulates EM wave transmission toward a multi-layer surface and identifies concealed targets based on reflection characteristics such as time delay and amplitude.

Inspired by Ground Penetrating Radar (GPR) systems, EMScope provides an interactive environment for research, education, and engineering applications.

---

## 🚀 Features

- 1D Finite Difference Time Domain (FDTD) EM simulation
- Configurable layered media
- Hidden object insertion
- Reflection analysis
- Depth estimation from time delay
- Extended material database (soil, water, concrete, metals, etc.)
- Conductivity and attenuation modeling
- Real-time wave propagation animation
- Receiver signal visualization
- GUI-based control panel
- Modular, research-oriented architecture

---

## 🧠 Physics Model

EMScope solves Maxwell’s equations using the Finite Difference Time Domain (FDTD) method.

Wave velocity in medium:

v = c / sqrt(εr)

Depth estimation formula:

d = (v × Δt) / 2

Where:
- c = speed of light
- εr = relative permittivity
- Δt = time delay between transmitted pulse and reflection

The simulation supports lossy media using conductivity parameters and stability via CFL condition enforcement.

---

## 📂 Project Structure

EMScope/
│
├── main.py
├── requirements.txt
│
├── core/                 # FDTD engine
│   ├── grid.py
│   ├── fdtd_solver.py
│   ├── source.py
│   ├── boundary.py
│   └── material.py
│
├── physics/              # EM equations & constants
│   ├── constants.py
│   ├── wave_equations.py
│   ├── reflection.py
│   └── attenuation.py
│
├── signal_processing/    # Detection algorithms
│   ├── peak_detection.py
│   ├── depth_estimation.py
│   └── noise_model.py
│
├── visualization/        # Plotting & animation
│   ├── plot_fields.py
│   ├── plot_signal.py
│   └── animation.py
│
├── gui/                  # User interface
│   ├── main_window.py
│   ├── controls_panel.py
│   └── results_panel.py
│
├── config/               # Materials & presets
│   ├── material_database.py
│   └── simulation_config.py
│
├── tests/                # Unit tests
│   ├── test_fdtd.py
│   └── test_reflection.py
│
└── docs/                 # Research papers & reports

---

## 🛠 Installation

### 1. Clone Repository

git clone https://github.com/your-username/EMScope.git  
cd EMScope  

### 2. Install Dependencies

pip install -r requirements.txt  

### 3. (Linux Only) Install Tkinter if missing

sudo apt install python3-tk  

---

## ▶ Run the Application

python main.py  

Check version:

python main.py --version  

---

## 🧪 Run Tests

pytest  

---

## 📡 Applications

- Ground Penetrating Radar (GPR)
- Civil engineering subsurface inspection
- Buried object detection
- Moisture sensing
- Concrete structure analysis
- Electromagnetic education & research

---

## 🔬 Research Scope & Future Extensions

- 2D / 3D FDTD simulation
- Perfectly Matched Layer (PML) absorbing boundaries
- Frequency sweep radar analysis
- Multi-receiver detection
- Inverse EM problem solving
- Machine learning-based material classification

---

## 📜 License

MIT License

---

## 👨‍💻 Project Vision

EMScope is designed as a structured electromagnetic subsurface sensing simulation framework that bridges theoretical EM physics and practical radar-based detection systems.

It is suitable for academic projects, research experimentation, and advanced simulation development.