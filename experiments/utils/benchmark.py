import statistics
from experiments.utils.timing import time_function


def measure(G, f, runs=10):
    times = []

    for _ in range(runs):
        _, t = time_function(f, G)
        times.append(t)

    return statistics.mean(times)
