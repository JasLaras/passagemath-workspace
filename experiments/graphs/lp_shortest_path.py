import time
from sage.numerical.mip import MixedIntegerLinearProgram

def run_lp(G, solver = "GLPK",measure_time = False):

    source = 0
    target = max(G.keys())
    
    # LP construction
    
    construction_start = time.perf_counter()

    p = MixedIntegerLinearProgram(maximization=False, solver=solver)

    x = p.new_variable(nonnegative=True)

    # Objective function
    p.set_objective(
        sum(
            w * x[u, v]
            for u in G
            for v, w in G[u]
        )
    )

    # Flow conservation constraints
    for node in G:

        inflow = sum(
            x[u, node]
            for u in G
            for v, w in G[u]
            if v == node
        )

        outflow = sum(
            x[node, v]
            for v, w in G[node]
        )

        if node == source:

            p.add_constraint(outflow - inflow == 1)

        elif node == target:

            p.add_constraint(inflow - outflow == 1)

        else:

            p.add_constraint(inflow == outflow)
    
    construction_end = time.perf_counter()

    # LP Solving 
    solve_start = time.perf_counter()

    p.solve()
    
    solve_end = time.perf_counter()
    
    objective = p.get_objective_value()

    construction_time = construction_end - construction_start
    solve_time = solve_end - solve_start
    total_time = construction_time + solve_time

    if measure_time:
        return objective, construction_time, solve_time, total_time

    return objective
