import json
import random
import statistics

from experiments.utils.graph_generator import random_graph
from experiments.utils.benchmark import measure

from experiments.graphs.dijkstra_test import run_dijkstra
from experiments.graphs.bellman_ford_test import run_bellman_ford
from experiments.graphs.lp_shortest_path import build_lp, solve_lp

# Reassign weights while keeping the same graph topology
def reweight_graph(G, weight_max):
    return {
        u: [
            (v, random.randint(1, weight_max))
            for v, _ in G[u]
        ]
        for u in G
    }

random.seed(42)

weight_ranges = [10, 100, 1000]
solvers = ["Highs", "GLPK", "Cvxpy"]
runs = 10

results = []

# Generate topology ONCE
base_G = random_graph(
    n=100,
    edge_prob=0.3,
    weight_max=10
)

for w in weight_ranges:

    print("\n" + "=" * 50)
    print("\nWeight Range:", w)
    print("=" * 50)

    # Same topology, new edge weights
    G = reweight_graph(base_G, weight_max=w)

    t_dijkstra = measure(G, run_dijkstra, runs=runs)
    t_bf = measure(G, run_bellman_ford, runs=runs)

    print("Dijkstra:", t_dijkstra)
    print("Bellman-Ford:", t_bf)

    results.append({
        "weight_max": w,
        "dijkstra": t_dijkstra,
        "bellman_ford": t_bf,
    })
    
    for solver in solvers:

        # Construct LP once
        p, x = build_lp(G, solver=solver)

        solve_times = []

        # Solve same formulation repeatedly
        for _ in range(runs):
            _, solve_time = solve_lp(p, x, G)
            solve_times.append(solve_time)

        t_lp = statistics.mean(solve_times)

        print(f"LP ({solver}):", t_lp)

        result[f"lp_{solver.lower()}"] = t_lp

    results.append(result)

with open("weight_results.json", "w") as f:
    json.dump(results, f, indent=4)