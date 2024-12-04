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
    diff_list = [x - y for x, y in zip(line, line[1:])]
    for current_diff in diff_list:
        has_less_than_zero |= current_diff < 0
        has_greater_than_zero |= current_diff > 0
        if has_less_than_zero and has_greater_than_zero:
            return False
        if -4 < current_diff < 4 and current_diff != 0:
            diffs.append(current_diff)
        else:
            return False
    return True


@time_it
def main():
    input_file = read_lines("input.txt")
    lines = [x.split() for x in input_file]
    numbers = [[int(i) for i in line] for line in lines]

    answer = sum(1 for number in numbers if check_line(number))
    print(answer)


if __name__ == "__main__":
    main()
