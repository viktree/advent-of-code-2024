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


def get_point(grid, r, c):
    return grid[r][c]


def up(bot):
    return (bot[0] - 1, bot[1])


def down(bot):
    return (bot[0] + 1, bot[1])


def left(bot):
    return (bot[0], bot[1] - 1)


def right(bot):
    return (bot[0], bot[1] + 1)


@time_it
def main():
    file = read_lines("input.txt")

    nRows, nCols = len(file), len(file[0])
    grid = {}
    obstacles = set({})
    bot = ()

    for r, c in itertools.product(range(nRows), range(nCols)):
        x = file[r][c]
        grid[(r, c)] = x
        if x == "#":
            obstacles.add((r, c))
        if x == "^":
            bot = (r, c)

    path = set({})
    next = up(bot)
    while bot in grid:
        while bot in grid and next not in obstacles:
            grid[bot] = "X"
            path.add(bot)
            bot, next = next, up(bot)
        next = bot
        while bot in grid and next not in obstacles:
            grid[bot] = "X"
            path.add(bot)
            bot, next = next, right(bot)
        next = bot
        while bot in grid and next not in obstacles:
            grid[bot] = "X"
            path.add(bot)
            bot, next = next, down(bot)
        next = bot
        while bot in grid and next not in obstacles:
            grid[bot] = "X"
            path.add(bot)
            bot, next = next, left(bot)
        next = bot

    print(len(path))


if __name__ == "__main__":
    main()
