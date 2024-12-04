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
    diffs = []
    has_less_than_zero, has_greater_than_zero = False, False
    for x, y in zip(line, line[1:]):
        current_diff = y - x
        has_less_than_zero |= current_diff < 0
        has_greater_than_zero |= current_diff > 0
        if has_less_than_zero and has_greater_than_zero:
            return False
        if -4 < current_diff < 4 and current_diff != 0:
            diffs.append(current_diff)
        else:
            return False
    return True


def partition(predicate, lst):
    true_list = []
    false_list = []

    for item in lst:
        if predicate(item):
            true_list.append(item)
        else:
            false_list.append(item)

    return true_list, false_list


@time_it
def main():
    input_file = read_lines("input.txt")
    lines = [x.split() for x in input_file]
    numbers = [[int(i) for i in line] for line in lines]

    good_lines, bad_lines = partition(check_line, numbers)

    for bad_line in bad_lines:
        is_fine_now = False
        for i, _ in enumerate(bad_line):
            line_without_i = bad_line[:i] + bad_line[i + 1 :]
            is_fine_now |= check_line(line_without_i)
        if is_fine_now:
            good_lines.append(bad_line)

    print(len(good_lines))


if __name__ == "__main__":
    main()
