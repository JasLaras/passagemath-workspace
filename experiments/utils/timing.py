import time

def time_function(func, *args, repeats=1, **kwargs):
    """
    Simple runtime measurement tool.
    """
    start = time.perf_counter()

    result = None
    for _ in range(repeats):
        result = func(*args, **kwargs)

    end = time.perf_counter()

    return result, (end - start) / repeats
