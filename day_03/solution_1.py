#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


def solve(line):
    answer = 0
    line = line.strip()
    # Find the largest two digits in the string, but they must read left to right.
    # E.g. "987654321111111" -> 9 and 8 -> 98
    digits = [int(d) for d in line]
    max_first = max(digits[:-1])
    first_index = digits.index(max_first)
    try:
        if first_index == len(digits) - 2:
            max_second = digits[-1]
        else:
            max_second = max(digits[first_index + 1 :])
    except Exception as e:
        print(f"Error processing line: {line}")
        print(f"  {digits=} {len(digits)=}")
        print(f"  {max_first=}")
        print(f"  {first_index=}")
        raise e
    answer = max_first * 10 + max_second
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

    sum = 0
    for line in lines:
        answer = solve(line)
        sum += answer
        print(f"Answer: {answer}")
    print(f"Sum of answers: {sum}")


if __name__ == "__main__":
    main()
