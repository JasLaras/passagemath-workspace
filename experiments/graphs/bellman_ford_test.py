def run_bellman_ford(G):
    """
    G is adjacency list:
    {node: [(neighbor, weight), ...]}
    """

    start = 0
    target = 2

    dist = {node: float('inf') for node in G}
    dist[start] = 0

    nodes = list(G.keys())

    # relax edges |V| - 1 times
    for _ in range(len(nodes) - 1):
        updated = False

        for u in G:
            for v, w in G[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True

        if not updated:
            break

    return dist[target]