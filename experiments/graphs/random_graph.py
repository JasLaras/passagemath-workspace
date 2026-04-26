from experiments.utils.graph_generator import random_graph
from experiments.utils.timing import time_function
from your_dijkstra_test import run_dijkstra
from your_lp_shortest_path import run_lp

sizes = [10, 20, 50, 100]

for n in sizes:
    G = random_graph(n)

    # swap graph into both tests
    print("\nGraph size:", n)

    _, t1 = time_function(run_dijkstra)
    _, t2 = time_function(run_lp)

    print("Dijkstra:", t1)
    print("LP:", t2)
