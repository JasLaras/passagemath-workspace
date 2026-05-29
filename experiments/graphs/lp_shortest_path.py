from sage.numerical.mip import MixedIntegerLinearProgram
from sage.graphs.digraph import DiGraph

def run_lp(G_dict):

    source = 0
    target = max(G_dict.keys())

    edges = []

    for u in G_dict:
        for v, w in G_dict[u]:
            edges.append((u, v, w))

    G = DiGraph()

    for u, v, w in edges:
        G.add_edge(u, v, w)

    p = MixedIntegerLinearProgram(maximization=False)

    x = p.new_variable(nonnegative=True)

    p.set_objective(
        sum(w * x[u, v] for u, v, w in edges)
    )

    for v in G.vertices():

        inflow = sum(
            x[u, v2]
            for u, v2, w in edges
            if v2 == v
        )

        outflow = sum(
            x[v2, u]
            for v2, u, w in edges
            if v2 == v
        )

        if v == source:
            p.add_constraint(outflow - inflow == 1)

        elif v == target:
            p.add_constraint(inflow - outflow == 1)

        else:
            p.add_constraint(inflow == outflow)

    p.solve()

    return p.get_objective_value()
