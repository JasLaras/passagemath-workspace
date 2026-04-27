# def run_lp(G):
#     return 0

from sage.all import MixedIntegerLinearProgram

def run_lp(G, source=0, target=1):
    p = MixedIntegerLinearProgram(maximization=False)
    dist = p.new_variable()

    # objective: shortest path to target
    p.set_objective(dist[target])

    # source constraint
    p.add_constraint(dist[source] == 0)

    # edge constraints
    for u, v, w in G.edges():
        p.add_constraint(dist[v] <= dist[u] + w)

    p.solve()

    return p.get_values(dist)[target]
