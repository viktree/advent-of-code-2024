#!/bin/python3

import functools
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


def read_lines(filename: str) -> list[str]:
    with open(filename) as my_file:
        input_file = my_file.read().strip().splitlines()
        return input_file


@time_it
def main():
    input_file = read_lines("input.txt")
    zipped = [t.split("   ") for t in input_file]

    firsts, seconds = [], []
    for item in zipped:
        x, y = item
        firsts.append(int(x))
        seconds.append(int(y))

    firsts, seconds = sorted(firsts), sorted(seconds)

    difference = sum([abs(xy[0] - xy[1]) for xy in zip(firsts, seconds)])
    print(difference)


if __name__ == "__main__":
    main()
