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


def update_list(dependency_lst, before, after):
    if after not in dependency_lst:
        dependency_lst[after] = set([before])
    else:
        if before in dependency_lst[after]:
            return dependency_lst
        dependency_lst[after].add(before)

    if before in dependency_lst:
        for second_order_dep in dependency_lst[before]:
            dependency_lst = update_list(dependency_lst, second_order_dep, after)
    return dependency_lst


@time_it
def main():
    lines = read_lines("input.txt")

    raw_rules = [f.split("|") for f in lines if "|" in f]
    raw_updates = [f.split(",") for f in lines if "," in f]

    prerequisites = {}
    postrequisites = {}

    for before, after in raw_rules:
        prerequisites = update_list(prerequisites, before, after)

    tmp = []

    for k, lst in prerequisites.items():
        for i, x in enumerate(lst):
            if x not in postrequisites:
                postrequisites[x] = set([k])
            else:
                postrequisites[x].add(k)
            if x not in prerequisites:
                tmp.append(x)
        if k not in postrequisites:
            postrequisites[k] = set([])

    for x in tmp:
        prerequisites[x] = []

    total = 0
    for update in raw_updates:
        violates = False
        for i, x in enumerate(update):
            before, after = update[:i], update[i + 1 :]
            for y in before:
                if y not in prerequisites[x]:
                    violates = True
                    break
            for y in after:
                if y not in postrequisites[x]:
                    violates = True
                    break
        if not violates:
            print(int(update[(len(update) - 1) // 2]))
            total += int(update[(len(update) - 1) // 2])
    print(total)


if __name__ == "__main__":
    main()
