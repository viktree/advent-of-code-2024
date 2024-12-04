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
        input_file = my_file.read().strip().split("\n")
        return input_file


def make_get_cross(nRows, nCols):
    def get_cross(i, j):
        direction = [
            (i - 1, j - 1),
            (i - 1, j + 1),
            (i + 1, j - 1),
            (i + 1, j + 1),
        ]
        for p in direction:
            row, col = p
            if row < 0 or col < 0 or row >= nRows or col >= nCols:
                return []
        return direction

    return get_cross


def grid_points(nRows, nCols):
    for point in itertools.product(range(nRows), range(nCols)):
        row, col = point
        yield row, col


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
    for row, col in grid_points(nRows, nCols):
        if lines[row][col] == "A":
            neighbors = get_cross(row, col)
            letter_count = Counter([get_letter(p) for p in neighbors])
            if (
                len(neighbors) == 4
                and letter_count["S"] == 2
                and letter_count["M"] == 2
                and get_letter(neighbors[0]) != get_letter(neighbors[3])
                and get_letter(neighbors[1]) != get_letter(neighbors[2])
            ):
                count += 1
    print(count)


if __name__ == "__main__":
    main()
