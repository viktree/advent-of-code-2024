#!/bin/python3


import functools
import itertools
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
        input_file = my_file.read().strip().split("\n")
        return input_file


def make_get_neighbors(nRows, nCols):
    def list_neighbors(i, j):
        direction_list = [
            [(i - 1, j - 1), (i - 2, j - 2), (i - 3, j - 3)],
            [(i - 1, j), (i - 2, j), (i - 3, j)],
            [(i - 1, j + 1), (i - 2, j + 2), (i - 3, j + 3)],
            [(i, j - 1), (i, j - 2), (i, j - 3)],
            [(i, j + 1), (i, j + 2), (i, j + 3)],
            [(i + 1, j - 1), (i + 2, j - 2), (i + 3, j - 3)],
            [(i + 1, j), (i + 2, j), (i + 3, j)],
            [(i + 1, j + 1), (i + 2, j + 2), (i + 3, j + 3)],
        ]
        filtered = []
        for direction in direction_list:
            for p in direction:
                row, col = p
                if row < 0 or col < 0 or row >= nRows or col >= nCols:
                    break
            else:
                filtered.append(direction)
        return filtered

    return list_neighbors


def grid_points(nRows, nCols):
    for point in itertools.product(range(nRows), range(nCols)):
        row, col = point
        yield row, col


@time_it
def main():
    lines = read_lines("input.txt")
    nRows, nCols = len(lines), len(lines[0])
    list_neighbors = make_get_neighbors(nRows, nCols)

    count = 0
    for row, col in grid_points(nRows, nCols):
        if lines[row][col] == "X":
            for direction in list_neighbors(row, col):
                if [lines[p[0]][p[1]] for p in direction] == ["M", "A", "S"]:
                    count += 1
    print(count)


if __name__ == "__main__":
    main()
