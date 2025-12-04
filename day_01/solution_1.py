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

    print(f"\nNumber of times dial hit zero: {num_zeroes}")


if __name__ == "__main__":
    main()
