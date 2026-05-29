from sage.numerical.mip import MixedIntegerLinearProgram

def run_lp(G):

    source = 0
    target = max(G.keys())

    p = MixedIntegerLinearProgram(maximization=False)

    x = p.new_variable(nonnegative=True)

    # objective function
    p.set_objective(
        sum(
            w * x[u, v]
            for u in G
            for v, w in G[u]
        )
    )

    # flow conservation
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

    p.solve()

    return p.get_objective_value()
