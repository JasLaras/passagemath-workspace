import random
import statistics
import time

from experiments.utils.graph_generator import random_graph
from experiments.graphs.lp_shortest_path import build_lp, solve_lp


random.seed(42)

sizes = [10, 20, 50, 100]
runs = 5


for n in sizes:

    G = random_graph(n)

    print("\n" + "=" * 50)
    print("Graph Size:", n)
    print("=" * 50)

    # Construct LP once
    construction_start = time.perf_counter()

    p = build_lp(G)

    construction_end = time.perf_counter()

    construction_time = construction_end - construction_start

    # Solve the same LP repeatedly
    solve_times = []

    for _ in range(runs):

        _, solve_time = solve_lp(p)

        solve_times.append(solve_time)

    avg_solve = statistics.mean(solve_times)
    total_solve = sum(solve_times)

    # Amortized construction cost
    amortized_construction = construction_time / runs

    total_repeated = construction_time + total_solve

    average_cost_per_run = total_repeated / runs

    # Results
    print("LP Construction (once):", construction_time)
    print("Average LP Solve:", avg_solve)
    print("Total Solve Time:", total_solve)
    print("Amortized Construction per Run:", amortized_construction)
    print("Average Total Cost per Run:", average_cost_per_run)
    print("Total Cost (Construction + All Solves):", total_repeated)