import os

import numpy as np

DIRECTORY = os.path.dirname(__file__)


def get_lines_from_file(file_path) -> list[str]:
    with open(os.path.join(DIRECTORY, file_path), "r") as f:
        return f.read().splitlines()


def part1(file_path):
    result = 0
    for line in get_lines_from_file(file_path):
        line_s: list[str] = list(line)
        line_ints = list(map(int, line))

        first_idx = np.argmax(np.array(line_ints[:-1]))
        available = line_ints[first_idx + 1 :]
        second_str = line_s[np.argmax(np.array(available)) + first_idx + 1]

        result += int(line_s[first_idx] + second_str)

    return result


def part2(file_path):
    result = 0
    for line in get_lines_from_file(file_path):
        line_arr = np.array(list(map(int, list(line))))
        result_str = ""
        number_taken = 0
        last_index = -1
        for i in range(1, 13):
            must_leave = 12 - i
            list_end = -must_leave if must_leave != 0 else len(line_arr)
            relative_index = np.argmax(line_arr[last_index + 1 : list_end])
            result_str += line[number_taken + relative_index]
            number_taken += 1 + relative_index
            last_index = number_taken - 1

        result += int(result_str)
    return result


if __name__ == "__main__":
    print(f"Part 1: {part1('./input/day3.txt')}")
    print(f"Part 2: {part2('./input/day3.txt')}")
