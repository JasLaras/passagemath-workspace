# Passagemath Lab Workspace – Optimization & Combinatorial Experiments

## Overview

This repository is my workspace for working in a mathematics research lab focused on **optimization, linear programming (LP), mixed-integer programming (MIP), and combinatorial algorithms**.

The project combines:

* Running **independent experiments** on optimization vs. graph/algorithmic methods
* Developing material for a **research thesis (20–30 pages)**

---

## Goals

* Understand and experiment with **linear programming and MIP**
* Explore connections between:

  * Optimization (LP/MIP)
  * Graph theory & combinatorics
  * Algorithms (e.g., shortest path, flow problems)
* Compare:

  * Optimization-based approaches (Passagemath)
  * Classical algorithms (implemented independently)
* Collect results (runtime, accuracy, structure) for analysis in a research paper

---

## Repository Structure

```
passagemath-workspace/
│
├── fork/                  # Fork of Passagemath (actual source code)
│
├── experiments/           # Independent testing and research code
│   ├── graphs/            # Dijkstra, flow, etc.
│   └── utils/             # Helpers (timing, logging, etc.)
│
└── README.md
```

---

## Passagemath Setup (Fork)

### 1. Fork and Clone

Fork the repository on GitHub, then:

```bash
git clone git@github.com:YOUR_USERNAME/passagemath.git fork
cd fork
```

---

### 2. Install `uv`

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

### 3. Create Environment

```bash
uv venv
```

---

### 4. Install a Package

Install only what you need (start with one):

```bash
uv pip install passagemath-combinat
# or
uv pip install passagemath-polyhedra
```

---

### 5. Run Code / Tests

Run a quick test:

```bash
uv run python -c "
from sage.combinat.partition import Partitions
print(Partitions(5).cardinality())
"
```

Run doctests:

```bash
uv run python -m sage.doctest src/sage/combinat/partition.py
```

---

### ⚠️ Troubleshooting (Build Dependencies)

Some systems may require additional dependencies for running doctests or building Passagemath modules.

If you encounter build or import errors, install the following:

#### Python build dependency

```bash
uv pip install meson-python
```

#### System-level dependency

```bash
sudo apt update
sudo apt install ninja-build
```

---

## Experiments Setup

### 1. Create environment

```bash
python3 -m venv pmath-env
```

### 2. Activate environment

```bash
source pmath-env/bin/activate
```

### 3. Install Passagemath (prebuilt library version)

```bash
pip install --prefer-binary passagemath-combinat
pip install --prefer-binary passagemath-polyhedra
```

### 4. Verify install

```bash
python -c "
from sage.combinat.partition import Partitions
print(Partitions(5).cardinality())
"
```
Should return ```7```.

---
