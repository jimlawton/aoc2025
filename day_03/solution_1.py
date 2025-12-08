#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


def solve(lines):
    answer = []
    return answer


def test():
    fails = 0
    print("\nRunning tests #1...")
    test_data = []
    for i, test_case in enumerate(test_data):
        print(f"  Test case {i + 1}:")
        answer = solve([test_case])
        expected_answer = []
        if answer == expected_answer:
            print("    PASS")
        else:
            print(f"    FAIL: expected {expected_answer}, got {answer}")
            fails += 1
        if sum(answer) == sum(expected_answer):
            print("    PASS sum")
        else:
            print(f"    FAIL: expected sum {sum(expected_answer)}, got {sum(answer)}")
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
