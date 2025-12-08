#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

# Initial dial position.
INITIAL = 50

# Dial size, steps.
SIZE = 100


def solve(lines):
    current = INITIAL
    total_zeros = 0

    print(f"Dial starts at position {current}")

    for rotation in lines:
        rotation = rotation.strip()
        direction = rotation[0]
        steps = int(rotation[1:])

        start_pos = current

        # Simulate each individual click
        for _ in range(steps):
            if direction == "L":
                current = (current - 1) % SIZE
            else:  # 'R'
                current = (current + 1) % SIZE

            if current == 0:
                total_zeros += 1

        print(f"Rotated {rotation} from {start_pos} to point at {current}")

    return total_zeros


def test():
    fails = 0

    print("\nRunning tests #1...")
    test_data = [["L50", "R50"], ["L50", "L50"], ["R50", "L50"], ["R50", "R50"]]
    for i, test_case in enumerate(test_data):
        print(f"\n  Test case {i + 1}:")
        current, zero_hits, zero_crossings = solve(test_case)
        if zero_hits == 1 and zero_crossings == 0:
            print("  PASS")
        else:
            fails += 1
            print(
                f"  FAIL: Test case expected 1 zero hit and no zero crossing, got {zero_hits}, {zero_crossings}"
            )

    print("\nRunning tests #2...")
    test_data = [["L150", "L50"], ["L150", "R50"], ["R150", "L50"], ["R150", "R50"]]
    for i, test_case in enumerate(test_data):
        print(f"\n  Test case {i + 1}:")
        current, zero_hits, zero_crossings = solve(test_case)
        if zero_hits == 1 and zero_crossings == 1:
            print("  PASS")
        else:
            fails += 1
            print(
                f"  FAIL: expected 1 zero hit and 1 zero crossing, got {zero_hits}, {zero_crossings}"
            )

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

    total_zeros = solve(lines)
    print(f"\nTotal times dial pointed at zero: {total_zeros}")


if __name__ == "__main__":
    main()
