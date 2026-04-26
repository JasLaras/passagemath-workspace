from experiments.utils.timing import time_function
from experiments.graphs.dijkstra_test import run_dijkstra
from experiments.graphs.lp_shortest_path import run_lp
from experiments.graphs.random_graph import random_graph

def run_both_on_graph(G):
    # inject graph into global functions (simple version)
    global graph_global
    graph_global = G

    _, t1 = time_function(run_dijkstra)
    _, t2 = time_function(run_lp)

    return t1, t2

def experiment():
    sizes = [5, 10, 20, 50]

    for n in sizes:
        G = random_graph(n)

        t_dijkstra, t_lp = run_both_on_graph(G)

        print("\nN =", n)
        print("Dijkstra:", t_dijkstra)
        print("LP:", t_lp)

if __name__ == "__main__":
    experiment()
