import json
import random

from experiments.utils.graph_generator import random_graph
from experiments.utils.benchmark import measure

from experiments.graphs.dijkstra_test import run_dijkstra
from experiments.graphs.bellman_ford_test import run_bellman_ford
from experiments.graphs.lp_shortest_path import run_lp

random.seed(42)

weight_ranges = [10, 100, 1000]

results = []

for w in weight_ranges:

    print("\nWeight Range:", w)

    G = random_graph(
        n=100,
        edge_prob=0.3,
        weight_max=w
    )

    t_dijkstra = measure(G, run_dijkstra)

    t_bf = measure(G, run_bellman_ford)

    t_lp = measure(G, run_lp)

    print("Dijkstra:", t_dijkstra)
    print("Bellman-Ford:", t_bf)
    print("LP:", t_lp)

    results.append({
        "weight_max": w,
        "dijkstra": t_dijkstra,
        "bellman_ford": t_bf,
        "lp": t_lp
    })

with open("weight_results.json", "w") as f:
    json.dump(results, f, indent=4)