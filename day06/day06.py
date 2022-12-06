import collections
import sys
import copy
from collections import defaultdict
from itertools import islice
from typing import Iterable


def window(seq: Iterable, n:int =2) -> Iterable:
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def calc_start(line: str, window_size: int =4) -> int:
    for seq in enumerate(window(line, window_size)):
        index, chars = seq
        if len(set(chars)) == len(chars):
            return index + window_size
    return -1


if __name__ == "__main__":
    with open(sys.argv[1], "r") as input_file:
        input_line = input_file.read().strip()
    part1 = calc_start(input_line)
    part2 = calc_start(input_line, 14)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
