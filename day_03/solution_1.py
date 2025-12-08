#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


def solve(line):
    answer = 0
    line = line.strip()
    # Find the largest two digits in the string, but they must read left to right.
    # E.g. "987654321111111" -> 9 and 8 -> 98
    first_digit = -1
    second_digit = -1
    for char in line:
        print(first_digit, second_digit)
        digit = int(char)
        print(digit)
        if digit > first_digit:
            first_digit = digit
        elif digit > second_digit and digit != first_digit:
            second_digit = digit
    if first_digit != -1 and second_digit != -1:
        answer = first_digit * 10 + second_digit
    return answer


def test():
    fails = 0
    print("\nRunning tests #1...")
    test_data = [
        ("987654321111111", 98),
        ("811111111111119", 89),
        ("234234234234278", 78),
        ("818181911112111", 92),
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

    if joltage_sum == 357:
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

    _answer = solve(lines)


if __name__ == "__main__":
    main()
