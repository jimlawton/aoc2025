#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


def solve(lines):
    repeats = []
    for line in lines:
        id_ranges = line.strip().split(",")
        for id_range in id_ranges:
            start_str, end_str = id_range.split("-")
            start = int(start_str)
            end = int(end_str)
            range_ids = list(range(start, end + 1))
            for id in range_ids:
                str_id = str(id)
                if len(str_id) % 2 == 0:
                    half_len = len(str_id) // 2
                    if str_id[0:half_len] == str_id[half_len:]:
                        repeats.append(id)
    return repeats


def test():
    fails = 0
    print("\nRunning tests #1...")
    test_data = [
        "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    ]
    for i, test_case in enumerate(test_data):
        print(f"  Test case {i + 1}:")
        repeats = solve([test_case])
        expected_repeats = [11, 22, 99, 1010, 1188511885, 222222, 446446, 38593859]
        if repeats == expected_repeats:
            print("    PASS")
        else:
            print(f"    FAIL: expected {expected_repeats}, got {repeats}")
            fails += 1
        if sum(repeats) == sum(expected_repeats):
            print("    PASS sum")
        else:
            print(f"    FAIL: expected sum {sum(expected_repeats)}, got {sum(repeats)}")
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

    repeats = solve(lines)
    print(f"Found {len(repeats)} repeated IDs: {repeats}")
    print(f"Sum of repeated IDs: {sum(repeats)}")


if __name__ == "__main__":
    main()
