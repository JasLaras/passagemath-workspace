import random

from experiments.utils.graph_generator import random_graph
from experiments.graphs.lp_shortest_path import run_lp


random.seed(42)

sizes = [10, 20, 50, 100]

for n in sizes:

    G = random_graph(n)

    objective, construction_time, solve_time, total_time = run_lp(
        G,
        measure_time=True
    )

    print("\nGraph Size:", n)
    print("LP Construction:", construction_time)
    print("LP Solve:", solve_time)
    print("LP Total:", total_time)