import math
import os

DIRECTORY = os.path.dirname(__file__)


def get_vals_from_file(file_path):
    with open(os.path.join(DIRECTORY, file_path), "r") as f:
        result = []
        for pair in f.readline().strip().split(","):
            a_str, b_str = pair.split("-")
            result.append((int(a_str), int(b_str)))
        return result


def part1_val_if_invalid(val):
    s = str(val)
    L = len(s)
    if L % 2 == 0 and s[: L // 2] == s[L // 2 :]:
        return val
    return 0


def part1_invalid_vals_from_range(val_pairs):
    return sum(map(part1_val_if_invalid, range(val_pairs[0], val_pairs[1] + 1)))


def get_valid_divisors(n):
    # returns divisors of n excluding n itself
    divs = []
    for d in range(1, int(math.sqrt(n)) + 1):
        if n % d == 0:
            divs.append(d)
            if d != n // d and n // d != n:
                divs.append(n // d)
    return divs


def part2_val_if_invalid(val, unit):
    s = str(val)
    repeater = s[0:unit]

    # starts with 0 = invalid ID
    if repeater[0] == "0":
        return 0

    if all(s[i : i + unit] == repeater for i in range(0, len(s), unit)):
        return val

    return 0


def part1(file_path):
    val_pairs = get_vals_from_file(file_path)
    result = sum(map(part1_invalid_vals_from_range, val_pairs))
    return result


def part2(file_path):
    result = 0
    for lo, hi in get_vals_from_file(file_path):
        for val in range(lo, hi + 1):
            for unit in get_valid_divisors(len(str(val))):
                if part2_val_if_invalid(val, unit) > 0:
                    result += val
                    break
    return result


if __name__ == "__main__":
    print(f"Part 1: {part1('./input/day2.txt')}")
    print(f"Part 2: {part2('./input/day2.txt')}")
