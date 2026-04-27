import heapq

def run_dijkstra(G):
    # G is adjacency list: {node: [(neighbor, weight), ...]}

    start = 0
    target = 2

    dist = {node: float('inf') for node in G}
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)

        if u == target:
            return d

        for v, w in G[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))

    return dist[target]