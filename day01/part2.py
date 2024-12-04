#!/bin/python3

import functools
import time
from collections import Counter


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


def read_lines(filename: str) -> list[str]:
    with open(filename) as my_file:
        input_file = my_file.read().strip().splitlines()
        return input_file


@time_it
def main():
    input_file = read_lines("input.txt")
    zipped = [t.split("   ") for t in input_file]

    firsts = [int(x[0]) for x in zipped]
    seconds = [int(x[1]) for x in zipped]

    firsts.sort()
    seconds.sort()
    counter = Counter(seconds)

    score = sum([xy[0] * counter[xy[0]] for xy in zip(firsts, seconds)])
    print(score)


if __name__ == "__main__":
    main()
