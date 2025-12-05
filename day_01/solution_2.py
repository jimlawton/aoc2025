#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

# Initial dial position.
INITIAL = 50

# Dial size, steps.
SIZE = 100


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit(1)

    file = sys.argv[1]
    if not os.path.exists(file):
        print(f"File not found: {file}")
        sys.exit(1)

    with open(file, "r") as f:
        lines = f.readlines()

    num_zeroes = 0
    current = INITIAL
    zero_crossings = 0
    print(f"Dial starts at position {current}")
    for rotation in lines:
        rotation = rotation.strip()
        direction = rotation[0]
        steps = int(rotation[1:])
        num_crossings = 0
        if direction == "L":
            # Rotating left
            steps = -steps
            if current + steps < 0:
                num_crossings = -((current + steps) // SIZE)
                if current == 0:
                    num_crossings -= 1 if num_crossings > 0 else 0
                print(
                    f"Crossed zero {num_crossings} times going left: {current} + {steps} < 0"
                )
        else:
            # Rotating right
            if current + steps > SIZE:
                num_crossings = (current + steps) // SIZE
                if current == 0:
                    num_crossings -= 1 if num_crossings > 0 else 0
                print(
                    f"Crossed zero {num_crossings} times going right: {current} + {steps} > {SIZE}"
                )
        zero_crossings += num_crossings

        new = (current + steps) % SIZE
        if new == 0:
            num_zeroes += 1

        # print(f"Rotated {rotation} from {current} to point at {new}")
        current = new

    print(f"\nNumber of times dial hit zero: {num_zeroes}")
    print(f"Number of times dial crossed zero: {zero_crossings}")
    print(f"Total: {num_zeroes + zero_crossings}")


if __name__ == "__main__":
    main()
