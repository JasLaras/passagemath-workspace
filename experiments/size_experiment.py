import json
import random
import statistics

from experiments.utils.graph_generator import random_graph
from experiments.utils.benchmark import measure

from experiments.graphs.dijkstra_test import run_dijkstra
from experiments.graphs.bellman_ford_test import run_bellman_ford
from experiments.graphs.lp_shortest_path import build_lp, solve_lp

random.seed(42)

sizes = [10, 20, 50, 100]

solvers = ["Highs", "GLPK", "Cvxpy"]
runs = 10

results = []

for n in sizes:

    print("\n" + "=" * 50)
    print("\nGraph Size:", n)
    print("=" * 50)

    G = random_graph(
        n=n,
        edge_prob=0.3,
        weight_max=10
    )

    # Combinatorial algorithms
    t_dijkstra = measure(G, run_dijkstra, runs=runs)
    t_bf = measure(G, run_bellman_ford, runs=runs)

    print("Dijkstra:", t_dijkstra)
    print("Bellman-Ford:", t_bf)
    
    result = {
        "nodes": n,
        "dijkstra": t_dijkstra,
        "bellman_ford": t_bf
    }
    
    # LP backends
    for solver in solvers:

        # Construction happens BEFORE timing
        p, x = build_lp(G, solver=solver)
        
        solve_times = []

        for _ in range(runs):
            _, solve_time = solve_lp(p, x, G)
            solve_times.append(solve_time)

        t_lp = statistics.mean(solve_times)

        print(f"LP ({solver}):", t_lp)

        result[f"lp_{solver.lower()}"] = t_lp

    results.append(result)

with open("size_results.json", "w") as f:
    json.dump(results, f, indent=4)
