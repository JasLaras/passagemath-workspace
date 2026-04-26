from sage.graphs.graph import Graph
import random

def random_graph(n, p=0.3, weight_range=(1,10)):
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < p:
                w = random.randint(*weight_range)
                edges.append((i,j,w))
    return Graph(edges, weighted=True)
