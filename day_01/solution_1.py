#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

# Initial dial position.
INITIAL = 50

# Dial size, steps.
SIZE = 100


def solve(lines):
    num_zeroes = 0
    current = INITIAL
    for rotation in lines:
        rotation = rotation.strip()
        direction = rotation[0]
        steps = int(rotation[1:])
        if direction == "L":
            steps = -steps

        new = (current + steps) % SIZE
        print(f"Rotated {rotation} from {current} to point at {new}")
        if new == 0:
            num_zeroes += 1
        current = new
    return current, num_zeroes


def test():
    fails = 0
    print("\nRunning tests #1...")
    test_data = [["L50", "R50"], ["L50", "L50"], ["R50", "L50"], ["R50", "R50"]]
    for i, test_case in enumerate(test_data):
        print(f"  Test case {i + 1}:")
        current, num_zeroes = solve(test_case)
        if num_zeroes == 1:
            print("  PASS")
        else:
            fails += 1
            print(f"  FAIL: expected 1 zero hit, got {num_zeroes}")

    print("\nRunning tests #2...")
    test_data = [["L150", "L50"], ["L150", "R50"], ["R150", "L50"], ["R150", "R50"]]
    for i, test_case in enumerate(test_data):
        print(f"  Test case {i + 1}:")
        current, num_zeroes = solve(test_case)
        if num_zeroes == 1:
            print("  PASS")
        else:
            fails += 1
            print(f"  FAIL: expected 1 zero hit, got {num_zeroes}.")

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

    current, num_zeroes = solve(lines)
    print(f"\nNumber of times dial hit zero: {num_zeroes}")


if __name__ == "__main__":
    main()
