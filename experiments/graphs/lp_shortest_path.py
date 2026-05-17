from sage.all import MixedIntegerLinearProgram

def run_lp(G, source=0, target=1):
    p = MixedIntegerLinearProgram(maximization=False)

    # x[u,v] = whether edge is used
    x = p.new_variable(nonnegative=True)

    # objective: minimize total weight
    p.set_objective(
        sum(w * x[u, v] for u, v, w in G.edges())
    )

    # flow conservation constraints
    for v in G.vertices():
        inflow = sum(x[u, v] for u, u2, _ in G.edges() if u2 == v)
        outflow = sum(x[v, u] for v2, u, _ in G.edges() if v2 == v)

        if v == source:
            p.add_constraint(outflow - inflow == 1)
        elif v == target:
            p.add_constraint(inflow - outflow == 1)
        else:
            p.add_constraint(inflow == outflow)

    p.solve()

    return p.get_objective_value()
