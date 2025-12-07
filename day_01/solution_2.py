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
    zero_hits = 0
    zero_crossings = 0
    print(f"Dial starts at position {current}")
    for rotation in lines:
        rotation = rotation.strip()
        # print(f"\nDEBUG: Processing rotation: {rotation}")
        direction = rotation[0]
        steps = int(rotation[1:])
        steps = -steps if direction == "L" else steps
        new = (current + steps) % SIZE
        num_crossings = 0
        if direction == "L":
            # Rotating left
            if current + steps < 0:
                num_crossings = -((current + steps) // SIZE)
                # print(f"DEBUG: num_crossings={num_crossings}")
                if current == 0:
                    num_crossings -= 1
                    # print(f"DEBUG: num_crossings={num_crossings}")
                print(
                    f"Crossed zero {num_crossings} times going left: {current} + {steps} < 0"
                )
        else:
            # Rotating right
            if current + steps > SIZE:
                num_crossings = (current + steps) // SIZE
                # print(f"DEBUG: num_crossings={num_crossings}")
                if current == 0 or new == 0:
                    num_crossings -= 1
                    # print(f"DEBUG: num_crossings={num_crossings}")
                print(
                    f"Crossed zero {num_crossings} times going right: {current} + {steps} > {SIZE}"
                )
        zero_crossings += num_crossings

        if new == 0:
            zero_hits += 1

        # print(f"Rotated {rotation} from {current} to point at {new}")
        current = new
    return current, zero_hits, zero_crossings


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

    current, zero_hits, zero_crossings = solve(lines)
    print(f"\nNumber of times dial hit zero: {zero_hits}")
    print(f"Number of times dial crossed zero: {zero_crossings}")
    print(f"Total: {zero_hits + zero_crossings}")


if __name__ == "__main__":
    main()
