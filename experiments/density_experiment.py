import json
import random
import statistics

from experiments.utils.graph_generator import random_graph
from experiments.utils.benchmark import measure

from experiments.graphs.dijkstra_test import run_dijkstra
from experiments.graphs.bellman_ford_test import run_bellman_ford
from experiments.graphs.lp_shortest_path import build_lp, solve_lp

random.seed(42)

edge_probs = [0.1, 0.3, 0.5, 0.8]
solvers = ["Highs", "GLPK", "Cvxpy"]
runs = 10

results = []

for edge_prob in edge_probs:

    print("\n" + "=" * 50)
    print("\nEdge Density:", edge_prob)
    print("=" * 50)

    G = random_graph(
        n=100,
        edge_prob=edge_prob,
        weight_max=10
    )

    t_dijkstra = measure(G, run_dijkstra, runs=runs)
    t_bf = measure(G, run_bellman_ford, runs=runs)

    print("Dijkstra:", t_dijkstra)
    print("Bellman-Ford:", t_bf)

    results.append({
        "edge_prob": edge_prob,
        "dijkstra": t_dijkstra,
        "bellman_ford": t_bf,
    })
    
    for solver in solvers:

        # Construct LP once
        p, x = build_lp(G, solver=solver)

        solve_times = []

        # Average solver execution time only
        for _ in range(runs):
            _, solve_time = solve_lp(p, x, G)
            solve_times.append(solve_time)

        t_lp = statistics.mean(solve_times)

        print(f"LP ({solver}):", t_lp)

        result[f"lp_{solver.lower()}"] = t_lp

    results.append(result)

with open("density_results.json", "w") as f:
    json.dump(results, f, indent=4)