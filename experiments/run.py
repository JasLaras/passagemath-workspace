from experiments.utils.benchmark import measure
from experiments.graphs.dijkstra_test import run_dijkstra
from experiments.graphs.bellman_ford_test import run_bellman_ford
from experiments.graphs.lp_shortest_path import run_lp
from experiments.utils.graph_generator import random_graph
import json


def run_both_on_graph(G):
    t_dijkstra = measure(G, run_dijkstra)
    t_bf = measure(G, run_bellman_ford)
    t_lp = measure(G, run_lp)
    return t_dijkstra, t_bf, t_lp


def experiment():
    sizes = [5, 10, 15, 20]
    # sizes = [5, 10, 20, 50]
    results = []

    for n in sizes:
        G = random_graph(n) # REPLACE n with values

        t_dijkstra, t_lp = run_both_on_graph(G)
        t_lp, _ = time_function(run_lp, G)
        _, t_bf = time_function(run_bellman_ford, G)

        print("\nN =", n)
        print("Dijkstra:", t_dijkstra)
        print("Bellman-Ford:", t_bf)
        print("LP:", t_lp)

        results.append({
            "n": n,
            "dijkstra_time": t_dijkstra,
            "bellman_ford_time:" t_bf, 
            "lp_time": t_lp
        })

    print("\nFinal Results:")
    for r in results:
        print(r)

    # save results into database 
    with open("results.json", "w") as f:
        json.dump(results, f, indent=4)


if __name__ == "__main__":
    experiment()