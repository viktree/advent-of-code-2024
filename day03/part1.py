#!/bin/python3


import functools
import re
import time


def time_it(func):
    """Decorator to measure and print the elapsed time of a function."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        t_start = time.perf_counter_ns()
        result = func(*args, **kwargs)
        t_stop = time.perf_counter_ns()
        print(f"Elapsed time: {t_stop - t_start} ns")
        return result

    return wrapper


@time_it
def main():
    with open("input.txt") as f:
        file = f.read()
        matches = re.findall(r"mul\((\d+),(\d+)\)", file)
        product = sum([int(x) * int(y) for x, y in matches])
        print(product)


if __name__ == "__main__":
    main()
