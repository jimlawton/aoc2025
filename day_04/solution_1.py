#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


def solve(line):
    answer = 0
    return answer


def test():
    fails = 0
    print("\nRunning tests #1...")
    test_data = []
    for i, (test_case, expected_answer) in enumerate(test_data):
        print(f"  Test case {i + 1}:")
        answer = solve(test_case)
        if answer == expected_answer:
            print("    PASS")
        else:
            print(f"    FAIL: expected {expected_answer}, got {answer}")
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

    for line in lines:
        _answer = solve(line)


if __name__ == "__main__":
    main()
