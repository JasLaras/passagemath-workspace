from sage.graphs.graph import Graph
from experiments.utils.timing import time_function

# small test graph
G = Graph([(0,1,1),(1,2,2),(0,2,5)], weighted=True)

def run_dijkstra(G):
    return graph_global.shortest_path(0, 2, by_weight=True)

result, runtime = time_function(run_dijkstra)

print("Shortest path (Dijkstra):", result)
print("Runtime:", runtime)
