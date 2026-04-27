import random

def random_graph(n, edge_prob=0.3):
    G = {i: [] for i in range(n)}

    for i in range(n):
        for j in range(n):
            if i != j and random.random() < edge_prob:
                weight = random.randint(1, 10)
                G[i].append((j, weight))

    return G