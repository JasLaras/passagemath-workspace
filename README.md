# Passagemath Lab Workspace – Optimization & Combinatorial Experiments

## Overview

This repository is my workspace for an undergraduate mathematics research project focused on **optimization, linear programming (LP), mixed-integer programming (MIP), and combinatorial algorithms**. The experiments support an accompanying undergraduate thesis completed through the UC Davis Math Lab in polyhedral geometry and optimization with Professor Matthias K¨oppe 

The project compares classical shortest-path algorithms with a linear programming formulation of the shortest-path problem.

The primary methods studied are:

* Dijkstra's algorithm
* Bellman-Ford algorithm
* A shortest-path linear programming formulation implemented with PassageMath

The LP formulation is evaluated using three optimization backends:
* HiGHS
* GLPK
* CVXPY

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
* Evaluate runtime behavior as graph characteristics change
* Compare different optimization backends used by the LP formulation
* Examine LP model construction time separately from solver execution time
* Collect reproducible experimental results for analysis in the accompanying thesis

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
│   ├── weight_experiment.py        # Edge-weight experiment
|   ├── lp_timing_experiment.py     # LP construction vs. solver timing
│   └── lp_repeated_runs.py         # Repeated LP execution experiments
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

Restart the shell after installation if necessary.
Check the installation with:

```bash
uv --version
```

### 3. Create an Environment

```bash
uv venv
```

Activate the environment if needed:

```bash
source .venv/bin/activate
```

### 4. Install Passagemath Packages

Install the packages needed for the research:

```bash
uv pip install passagemath-combinat
uv pip install passagemath-polyhedra
```

The LP experiments additionally require the HiGHS, GLPK, and CVXPY optimization backends.
They can be installed through the PassageMath polyhedra extras:

```bash
uv pip install "passagemath-polyhedra[highs,glpk,cvxpy]"
```

If `passagemath-polyhedra` is already installed, running the command again adds the requested optional solver dependencies.

### 5. Checking Solvers

Before running the LP experiments, verify that PassageMath can create each required optimization backend.
From the active environment:

```bash
python - <<'PY'
from sage.numerical.backends.generic_backend import get_solver

solvers = ["Highs", "GLPK", "Cvxpy"]

for solver in solvers:
    try:
        backend = get_solver(solver=solver)
        print(f"{solver}: available ({type(backend).__name__})")
    except Exception as error:
        print(f"{solver}: unavailable")
        print(f"  {error}")
PY
```

A working environment should report backends corresponding to:

```bash
HiGHS
GLPK
CVXPY
```

The available backend can also be tested directly through `MixedIntegerLinearProgram`:

```bash
python - <<'PY'
from sage.numerical.mip import MixedIntegerLinearProgram

for solver in ["Highs", "GLPK", "Cvxpy"]:
    try:
        MixedIntegerLinearProgram(solver=solver)
        print(f"{solver}: OK")
    except Exception as error:
        print(f"{solver}: FAILED")
        print(error)
PY
```

### 6. Installing Missing Solvers

If one or more backends are unavailable, install the corresponding PassageMath optional dependency.

#### HiGHS
```bash
uv pip install "passagemath-polyhedra[highs]"
```

#### GLPK

```bash
uv pip install "passagemath-polyhedra[glpk]"
```

#### CVXPY

```bash
uv pip install "passagemath-polyhedra[cvxpy]"
```

All three can be installed together with:

```bash
uv pip install "passagemath-polyhedra[highs,glpk,cvxpy]"
```

After installation, rerun the solver-availability check before running the experiments.

### 7. Verify the Installation

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

The optimization framework can also be verified with:

```bash
uv run python -c "
from sage.numerical.mip import MixedIntegerLinearProgram
p = MixedIntegerLinearProgram(maximization=False, solver='Highs')
print(type(p.get_backend()).__name__)
"
```

---

## Troubleshooting

### `python` Command Not Found
Some Ubuntu installations expose Python only as python3.

Check with:
```bash
python3 --version
```
If the PassageMath virtual environment is active, its Python executable should normally be available directly as:
```bash
python
```
The executable being used can be checked with:
```bash
which python
```
Some systems may require additional build dependencies when working directly with the Passagemath source repository.

### Missing Python Build Dependency
If a build reports that `meson-python` is missing:
```bash
uv pip install meson-python
```

### Missing Ninja Build Tool
On Ubuntu:

```bash
sudo apt update
sudo apt install ninja-build
```

---

## Thesis and Presentation

The `thesis/` directory contains the LaTeX source for the accompanying undergraduate thesis.

The `presentation/` directory contains materials from the mid-quarter MAT 199 presentation in spring.

The complete source code and experimental results are maintained in this repository for reproducibility.
