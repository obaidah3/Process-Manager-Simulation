# 🚀 Process Manager Simulation 🏭🖥️

**A clean, professional simulation of CPU scheduling and memory paging, illustrating core Operating Systems concepts in Python.**

---

## 📑 Table of Contents

1. [Overview](#overview)
2. [✨ Features](#features)
3. [🛠️ Requirements](#requirements)
4. [📥 Installation](#installation)
5. [▶️ Usage](#usage)
6. [⚙️ Configuration](#configuration)
7. [📂 Project Structure](#project-structure)
8. [📊 Sample Output](#sample-output)
9. [🤝 Contributing](#contributing)
10. [📜 License](#license)
11. [👤 Author](#author)

---

## Overview

This repository provides **Process Manager Simulation**—a Python-based tool that models and executes various CPU scheduling algorithms (FCFS, SJF, Priority, Round Robin) alongside a simple memory paging mechanism. It is designed as an educational utility for learning or demonstration purposes, with a focus on clarity, configurability, and minimal dependencies.

---

## ✨ Features

* **🖥️ Process Modeling**: Each process has attributes including ID, name, grade, CPU burst time, priority, and memory page requirements.
* **📦 Memory Paging Simulation**: Allocates 1–3 pages per process, tracks page faults 🚨, and frees pages on termination.
* **📋 Scheduling Algorithms**:

  * 🕐 First-Come-First-Serve (FCFS)
  * 📏 Shortest Job First (SJF)
  * ⭐ Priority Scheduling
  * 🔄 Round Robin (RR) with configurable time quantum
* **🤖 Automated Demo**: Preloads sample processes and sequentially runs all scheduling strategies via a single method (`run_all()`).
* **⏱️ Adjustable Speed**: Control the simulation pacing with a `delay` parameter on initialization.
* **💾 Persistence**: Stores added processes in `processes.txt` for reuse across runs.

---

## 🛠️ Requirements

* **🐍 Python**: Version 3.7 or higher
* **📚 Standard Library**: No external dependencies (uses `random`, `time`, and file I/O)

---

## 📥 Installation

1. **🔗 Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/process-manager.git
   cd process-manager
   ```
2. **✅ Ensure Python 3.7+ is installed**.

---

## ▶️ Usage

1. **🚀 Run the simulation**:

   ```bash
   python process_manager.py
   ```
2. **📋 What Happens**: The program will:

   * 📂 Load or create `processes.txt`.
   * ➕ Add sample processes (Alice, Bob, Charlie) if none exist.
   * 👀 Display active processes.
   * 🏷️ Execute FCFS, SJF, Priority, and Round Robin scheduling.
   * 📈 Display completed processes and summary statistics.

---

## ⚙️ Configuration

* **✏️ Custom Processes**: Modify the `add_sample_processes()` method in `process_manager.py` to define your own set of processes.
* **⏳ Simulation Speed**: Adjust the `delay` argument when instantiating `ProcessManager`:

  ```python
  from process_manager import ProcessManager
  pm = ProcessManager(delay=0.05)
  pm.run_all()
  ```
* **🔢 Time Quantum**: Change the argument passed to `round_robin(time_quantum=...)` in `run_all()` or call `round_robin()` directly.

---

## 📂 Project Structure

```
process-manager/
├── processes.txt            # 💾 Persistent process data
├── process_manager.py       # 📝 Main simulation script
└── README.md                # 📖 Project documentation
```

---

## 📊 Sample Output

```text
No existing data (processes.txt). Starting fresh.
Added: Process ID: 001, Name: Alice, Grade: 85.0, State: New, CPU Burst: 3, Priority: 2, Memory Pages: 2, Page Faults: 0
...
== FCFS Scheduling ==
Allocating 2 pages for Alice...
-- Executing Alice (001) for 3 units.
[Time 1] Alice: 1/3 units, Faults: 0
...
*** Alice completed.
...
Total CPU Time: 9 units.
Completed: 3 processes. Page Faults: 1
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. 🍴 Fork this repository.
2. 🌿 Create a feature branch: `git checkout -b feature/YourFeature`.
3. 💬 Commit your changes: `git commit -m "Add YourFeature"`.
4. 📤 Push to your branch: `git push origin feature/YourFeature`.
5. 🔀 Open a pull request and describe your changes.

---

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

