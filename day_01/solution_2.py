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
    test_data = [
        (["L50", "R50"], 1),  # L50: 50->0 (1), R50: 0->50 (0) = 1 total
        (["L50", "L50"], 1),  # L50: 50->0 (1), L50: 0->50 (0) = 1 total
        (["R50", "L50"], 1),  # R50: 50->0 (1), L50: 0->50 (0) = 1 total
        (["R50", "R50"], 1),  # R50: 50->0 (1), R50: 0->50 (0) = 1 total
    ]
    for i, (test_case, expected) in enumerate(test_data):
        print(f"\n  Test case {i + 1}:")
        total = solve(test_case)
        if total == expected:
            print(f"  PASS (got {total})")
        else:
            fails += 1
            print(f"  FAIL: expected {expected}, got {total}")

    print("\nRunning tests #2...")
    test_data = [
        (
            ["L150", "L50"],
            2,
        ),  # L150: crosses 0 once + ends at 0, L50: 0->50 (0) = 2 total
        (
            ["L150", "R50"],
            2,
        ),  # L150: crosses 0 once + ends at 0, R50: 0->50 (0) = 2 total
        (
            ["R150", "L50"],
            2,
        ),  # R150: crosses 0 once + ends at 0, L50: 0->50 (0) = 2 total
        (
            ["R150", "R50"],
            2,
        ),  # R150: crosses 0 once + ends at 0, R50: 0->50 (0) = 2 total
    ]
    for i, (test_case, expected) in enumerate(test_data):
        print(f"\n  Test case {i + 1}:")
        total = solve(test_case)
        if total == expected:
            print(f"  PASS (got {total})")
        else:
            fails += 1
            print(f"  FAIL: expected {expected}, got {total}")

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
