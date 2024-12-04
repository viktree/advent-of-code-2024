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


def check_line(line):
    diffs = [y - x for x, y in zip(line, line[1:])]
    all_negative = all([x in [-3, -2, -1] for x in diffs])
    all_positive = all(x in [1, 2, 3] for x in diffs)
    return all_negative or all_positive


@time_it
def main():
    input_file = read_lines("input.txt")
    lines = [x.split() for x in input_file]
    numbers = [[int(i) for i in line] for line in lines]

    answer = sum(1 for number in numbers if check_line(number))
    print(answer)


if __name__ == "__main__":
    main()
