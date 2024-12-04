#!/bin/python3


import functools
import itertools
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


def make_get_cross(nRows, nCols):
    all_points = set([p for p in grid_points(nRows, nCols)])

    def get_cross(point):
        r, c = point
        direction = [
            (r - 1, c - 1),
            (r - 1, c + 1),
            (r + 1, c - 1),
            (r + 1, c + 1),
        ]
        for p in direction:
            if p not in all_points:
                return []
        return direction

    return get_cross


def grid_points(nRows, nCols):
    for point in itertools.product(range(nRows), range(nCols)):
        yield point


def make_get_letter(lines):
    def get_letter(p):
        return lines[p[0]][p[1]]

    return get_letter


@time_it
def main():
    lines = read_lines("input.txt")
    nRows, nCols = len(lines), len(lines[0])
    get_cross = make_get_cross(nRows, nCols)
    get_letter = make_get_letter(lines)

    count = 0
    for p in grid_points(nRows, nCols):
        if get_letter(p) == "A":
            neighbors = get_cross(p)
            letter_count = Counter([get_letter(q) for q in neighbors])
            if (
                letter_count["S"] == 2
                and letter_count["M"] == 2
                and get_letter(neighbors[0]) != get_letter(neighbors[3])
                and get_letter(neighbors[1]) != get_letter(neighbors[2])
            ):
                count += 1
    print(count)


if __name__ == "__main__":
    main()
