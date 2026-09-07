import random
import statistics
import time

from experiments.utils.graph_generator import random_graph
from experiments.graphs.lp_shortest_path import build_lp, solve_lp


random.seed(42)

sizes = [10, 20, 50, 100]
runs = 5
solvers = ["Highs", "GLPK", "Cvxpy"]

for n in sizes:

    G = random_graph(n)

    print("\n" + "=" * 50)
    print("Graph Size:", n)
    print("=" * 50)

    for solver in solvers:

        construction_times = []
        solve_times = []
        total_times = []

        for _ in range(runs):

            # Measure LP construction
            construction_start = time.perf_counter()

            p, x = build_lp(G, solver=solver)

            construction_end = time.perf_counter()

            construction_time = (
                construction_end - construction_start
            )

            # Measure LP solve
            _, solve_time = solve_lp(p, x, G)

            total_time = construction_time + solve_time

            construction_times.append(construction_time)
            solve_times.append(solve_time)
            total_times.append(total_time)
        
        avg_construction = statistics.mean(construction_times)
        avg_solve = statistics.mean(solve_times)
        avg_total = statistics.mean(total_times)

        # solver_name = "Default" if solver is None else solver

        print("\nSolver:", solver)
        print("\nGraph Size:", n)
        print("Average LP Construction:", avg_construction)
        print("Average LP Solve:", avg_solve)
        print("Average LP Total:", avg_total)