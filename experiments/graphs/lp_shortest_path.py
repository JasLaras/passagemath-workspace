def run_lp(G):
    return 0


# from sage.graphs.graph import Graph
# from experiments.utils.timing import time_function
# from scipy.optimize import linprog

# def solve_lp_shortest_path(G, source, target):
#    nodes = list(G.vertices())
#    n = len(nodes)

#    index = {v:i for i,v in enumerate(nodes)}

#    edges = [(u,v,d['label']) for u,v,d in G.edges(data=True)]

    # objective: minimize dist[target]
#    c = [0]*n
#    c[index[target]] = 1

#    A = []
#    b = []

    # constraints: dist[v] - dist[u] <= w(u,v)
#    for u,v,w in edges:
#        row = [0]*n
#        row[index[v]] = 1
#        row[index[u]] = -1
#        A.append(row)
#        b.append(w)

    # fix source: dist[source] = 0
#    A_eq = [[0]*n]
#    A_eq[0][index[source]] = 1
#    b_eq = [0]

#    res = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq)

#    return res.fun, res.x

# test graph
# G = Graph([(0,1,1),(1,2,2),(0,2,5)], weighted=True)

# def run_lp():
#    return solve_lp_shortest_path(graph_global, 0, 2)

# result, runtime = time_function(run_lp)

# print("LP shortest path value:", result)
# print("Runtime:", runtime)
