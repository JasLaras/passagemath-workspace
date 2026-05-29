import json

from experiments.utils.graph_generator import random_graph
from experiments.utils.benchmark import measure

from experiments.graphs.dijkstra_test import run_dijkstra
from experiments.graphs.bellman_ford_test import run_bellman_ford
from experiments.graphs.lp_shortest_path import run_lp


sizes = [10, 20, 50, 100]

results = []

for n in sizes:

    print("\nGraph Size:", n)

    G = random_graph(
        n=n,
        edge_prob=0.3,
        weight_max=10
    )

    t_dijkstra = measure(G, run_dijkstra)

    t_bf = measure(G, run_bellman_ford)

    t_lp = measure(G, run_lp)

    print("Dijkstra:", t_dijkstra)
    print("Bellman-Ford:", t_bf)
    print("LP:", t_lp)

    results.append({
        "nodes": n,
        "dijkstra": t_dijkstra,
        "bellman_ford": t_bf,
        "lp": t_lp
    })

with open("size_results.json", "w") as f:
    json.dump(results, f, indent=4)
