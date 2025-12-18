#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


def solve(line):
    answer = 0
    line = line.strip()
    # Find the largest twelve digits in the string, but they must read left to right.
    digits = [int(d) for d in line]
    n = len(digits)
    if n < 12:
        return 0
    result = []
    start_index = 0
    for pos in range(12):
        remaining_needed = 12 - pos - 1
        search_end = n - remaining_needed
        max_digit = max(digits[start_index:search_end])
        for i in range(start_index, search_end):
            if digits[i] == max_digit:
                result.append(max_digit)
                start_index = i + 1
                break

    answer = int("".join(map(str, result)))
    return answer


def test():
    fails = 0
    print("\nRunning tests #1...")
    test_data = [
        ("987654321111111", 987654321111),
        ("811111111111119", 811111111119),
        ("234234234234278", 434234234278),
        ("818181911112111", 888911112111),
    ]

    joltage_sum = 0
    for i, (test_case, expected_answer) in enumerate(test_data):
        print(f"  Test case {i + 1}:")
        answer = solve(test_case)
        joltage_sum += answer
        if answer == expected_answer:
            print("    PASS")
        else:
            print(f"    FAIL: expected {expected_answer}, got {answer}")
            fails += 1

    if joltage_sum == 3121910778619:
        print("    PASS sum")
    else:
        print(f"    FAIL: expected sum 357, got {joltage_sum}")
        fails += 1

    if fails == 0:
        print("\nAll tests PASS.")
    else:
        print(f"\n{fails} tests FAIL.")


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        test()
        sys.exit(0)

    file = sys.argv[1]
    if not os.path.exists(file):
        print(f"File not found: {file}")
        sys.exit(1)

    with open(file, "r") as f:
        lines = f.readlines()

    sum = 0
    for line in lines:
        answer = solve(line)
        sum += answer
        print(f"Answer: {answer}")
    print(f"Sum of answers: {sum}")


if __name__ == "__main__":
    main()
