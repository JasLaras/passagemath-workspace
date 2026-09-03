import random
import statistics
import time

from experiments.utils.graph_generator import random_graph
from experiments.graphs.dijkstra_test import run_dijkstra
from experiments.graphs.bellman_ford_test import run_bellman_ford

random.seed(42)

sizes = [10, 20, 50, 100]
runs = 5

for n in sizes:
    G = random_graph(n)

    print("\n" + "=" * 50)
    print("Graph Size:", n)
    print("=" * 50)

    dijkstra_times = []
    bellman_ford_times = []

    for _ in range(runs):

        start = time.perf_counter()
        run_dijkstra(G)
        end = time.perf_counter()
        dijkstra_times.append(end - start)

        start = time.perf_counter()
        run_bellman_ford(G)
        end = time.perf_counter()
        bellman_ford_times.append(end - start)

    print("\nDijkstra")
    print("Average:", statistics.mean(dijkstra_times))

    print("\nBellman-Ford")
    print("Average:", statistics.mean(bellman_ford_times))