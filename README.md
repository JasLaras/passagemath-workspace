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

  * A linear programming approach implemented using PassageMath
  * Classical shortest-path algorithms implemented independently in Python
* Evaluating runtime behavior as graph characteristics change
* Collecting reproducible experimental results for analysis in the accompanying thesis

---

## Repository Structure

```
passagemath-workspace/
│
├── fork/                           # Passagemath source code
│
├── experiments/                    # Experimental implementations and tests
│   ├── graphs/
│   │   ├── bellman_ford_test.py    # Bellman-Ford implementation
│   │   ├── dijkstra_test.py        # Dijkstra implementation
│   │   └── lp_shortest_path.py     # Linear programming formulation
│   │
│   ├── utils/
│   │   ├── benchmark.py            # Runtime benchmarking
│   │   ├── graph_generator.py      # Random graph generation
│   │   └── timing.py               # Timing utility
│   │
│   ├── density_experiment.py       # Edge-density experiment
│   ├── size_experiment.py          # Graph-size experiment
│   └── weight_experiment.py        # Edge-weight experiment
│
├── presentation/                   # Math Lab presentation materials
│
├── thesis/                         # Thesis LaTeX source
│
├── density_results.json            # Density experiment results
├── size_results.json               # Graph-size experiment results
├── weight_results.json             # Edge-weight experiment results
├── results.json                    # Earlier/general experiment results
└── README.md
```

---

# Passagemath Lab Workspace – Optimization & Combinatorial Experiments

## Overview

This repository contains my workspace for undergraduate mathematics research in **optimization, linear programming (LP), mixed-integer programming (MIP), and combinatorial algorithms**.

The primary project studies the shortest-path problem by comparing two classical combinatorial algorithms, Dijkstra's algorithm and Bellman-Ford, with a linear programming formulation implemented using PassageMath.

The repository also contains materials for the accompanying undergraduate thesis and research presentation.

---

## Goals

The project focuses on:

* Understanding linear programming and optimization through computational experimentation
* Exploring connections between:

  * Linear programming and network flow
  * Graph theory and combinatorics
  * Classical shortest-path algorithms
* Comparing:

  * A linear programming approach implemented using PassageMath
  * Classical shortest-path algorithms implemented independently in Python
* Evaluating runtime behavior as graph characteristics change
* Collecting reproducible experimental results for analysis in the accompanying thesis

---

## Repository Structure

```text
passagemath-workspace/
│
├── fork/                           # Passagemath source code
│
├── experiments/                    # Experimental implementations and scripts
│   ├── graphs/
│   │   ├── __init__.py
│   │   ├── bellman_ford_test.py    # Bellman-Ford implementation
│   │   ├── dijkstra_test.py        # Dijkstra implementation
│   │   └── lp_shortest_path.py     # LP shortest-path formulation
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── benchmark.py            # Runtime benchmarking
│   │   ├── graph_generator.py      # Random graph generation
│   │   └── timing.py               # Timing utility
│   │
│   ├── __init__.py
│   ├── density_experiment.py       # Edge-density experiment
│   ├── size_experiment.py          # Graph-size experiment
│   └── weight_experiment.py        # Edge-weight experiment
│
├── presentation/                   # Math Lab presentation materials
│
├── thesis/                         # Thesis LaTeX source
│
├── density_results.json            # Edge-density results
├── size_results.json               # Graph-size results
├── weight_results.json             # Edge-weight results
├── results.json                    # Earlier experimental results
├── .gitignore
├── .gitmodules
└── README.md
```

---
## Experiments

The experiments evaluate runtime performance while varying three characteristics of randomly generated weighted directed graphs.

### 1. Graph Size

The graph-size experiment varies the number of vertices:

```text
10, 20, 50, 100
```

Run with:

```bash
python -m experiments.size_experiment
```

### 2. Edge Density

The density experiment varies the probability that a directed edge is included in the graph:

```text
0.1, 0.3, 0.5, 0.8
```

Run with:

```bash
python -m experiments.density_experiment
```

### 3. Edge-Weight Range

The weight experiment varies the maximum randomly generated edge weight:

```text
1–10, 1–100, 1–1000
```

Run with:

```bash
python -m experiments.weight_experiment
```

A fixed random seed is used in the experiments to make graph generation reproducible.

For each experiment, the generated graph is supplied to all three approaches so that their runtimes can be compared using the same graph instance. Runtime measurements are performed using the benchmarking utilities in `experiments/utils/`.

---

## Experimental Results

The experiment scripts produce runtime measurements in seconds for Dijkstra, Bellman-Ford, and the LP formulation.

Results are stored in JSON files:

```text
size_results.json
density_results.json
weight_results.json
```

These files contain the data used for the runtime and scalability analysis in the accompanying thesis.

---

## Running the Experiments

From the repository root:

```bash
python -m experiments.size_experiment
```

```bash
python -m experiments.density_experiment
```

```bash
python -m experiments.weight_experiment
```

The experiments require the Python dependencies used by the implementations, including PassageMath for the linear programming formulation.

---

## Passagemath Setup

The `fork/` directory contains the Passagemath source repository used for research and exploration of the underlying project.

### 1. Fork and Clone

Fork the Passagemath repository on GitHub, then clone it into the workspace:

```bash
git clone git@github.com:YOUR_USERNAME/passagemath.git fork
cd fork
```

### 2. Install `uv`

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. Create an Environment

```bash
uv venv
```

### 4. Install Passagemath Packages

Install the packages needed for the research:

```bash
uv pip install passagemath-combinat
uv pip install passagemath-polyhedra
```

### 5. Verify the Installation

```bash
uv run python -c "
from sage.combinat.partition import Partitions
print(Partitions(5).cardinality())
"
```

The expected output is:

```text
7
```

---

## Troubleshooting

Some systems may require additional build dependencies when working directly with the Passagemath source repository.

### Python Build Dependency

```bash
uv pip install meson-python
```

### System Dependency

```bash
sudo apt update
sudo apt install ninja-build
```

---

## Thesis and Presentation

The `thesis/` directory contains the LaTeX source for the accompanying undergraduate thesis.

The `presentation/` directory contains materials from the Mid-quarter MAT 199 presentation in spring.

The complete source code and experimental results are maintained in this repository for reproducibility.
