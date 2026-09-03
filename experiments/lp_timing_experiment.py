import random
import statistics

from experiments.utils.graph_generator import random_graph
from experiments.graphs.lp_shortest_path import run_lp


random.seed(42)

sizes = [10, 20, 50, 100]
runs = 5
solvers = [None, "GLPK"]

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

            _, construction_time, solve_time, total_time = run_lp(
            G,
            solver=solver,
            measure_time=True
            )

            construction_times.append(construction_time)
            solve_times.append(solve_time)
            total_times.append(total_time)
        
        avg_construction = statistics.mean(construction_times)
        avg_solve = statistics.mean(solve_times)
        avg_total = statistics.mean(total_times)

        solver_name = "Default" if solver is None else solver

        print("\nSolver:", solver_name)
        print("\nGraph Size:", n)
        print("Average LP Construction:", avg_construction)
        print("Average LP Solve:", avg_solve)
        print("Average LP Total:", avg_total)