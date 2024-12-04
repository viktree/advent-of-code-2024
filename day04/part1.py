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
        input_file = my_file.read().strip().splitlines()
        return input_file


def make_get_neighbors(nRows: int, nCols: int):
    all_points = set([p for p in grid_points(nRows, nCols)])

    def list_neighbors(point):
        r, c = point
        direction_list = [
            [(r - 1, c - 1), (r - 2, c - 2), (r - 3, c - 3)],
            [(r - 1, c), (r - 2, c), (r - 3, c)],
            [(r - 1, c + 1), (r - 2, c + 2), (r - 3, c + 3)],
            [(r, c - 1), (r, c - 2), (r, c - 3)],
            [(r, c + 1), (r, c + 2), (r, c + 3)],
            [(r + 1, c - 1), (r + 2, c - 2), (r + 3, c - 3)],
            [(r + 1, c), (r + 2, c), (r + 3, c)],
            [(r + 1, c + 1), (r + 2, c + 2), (r + 3, c + 3)],
        ]
        filtered = []
        for direction in direction_list:
            for p in direction:
                if p not in all_points:
                    break
            else:
                filtered.append(direction)
        return filtered

    return list_neighbors


def grid_points(nRows, nCols):
    for point in itertools.product(range(nRows), range(nCols)):
        yield point


def make_get_letter(lines):
    def get_letter(p):
        r, c = p
        return lines[r][c]

    return get_letter


@time_it
def main():
    lines = read_lines("input.txt")

    nRows, nCols = len(lines), len(lines[0])
    list_neighbors = make_get_neighbors(nRows, nCols)
    get_letter = make_get_letter(lines)

    count = 0
    for s in grid_points(nRows, nCols):
        if get_letter(s) == "X":
            for direction in list_neighbors(s):
                if [get_letter(p) for p in direction] == ["M", "A", "S"]:
                    count += 1
    print(count)


if __name__ == "__main__":
    main()
