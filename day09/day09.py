import sys
from itertools import islice
from collections.abc import Iterable
from typing import Tuple
import networkx
from operator import add, mul






if __name__ == "__main__":
    with open(sys.argv[1], "r") as input_file:
        input_lines = input_file.read().splitlines()


        DIRECTIONS = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

        rope_head = (0, 0)
        rope_tail = (0, 0)

        visited = {(0, 0)}   # already contains the start  - using a set as we only count each visited place once
        # - defaultdict and adding would also work! in case part2 requiries it :D

        for line in input_lines:
            cur_dir, steps = line.split(" ")
            steps = int(steps)
            delta = DIRECTIONS[cur_dir]  # offset to current h_x, h_y
            for s in range(steps):
                rope_head = tuple(map(add, rope_head, delta))
                # check if we need to move:
                while max(abs(rope_tail[0] - rope_head[0]), abs(rope_tail[1] - rope_head[1 ])) > 1:
                    for i in range(2):
                        if abs(rope_tail[i] - rope_head[i]) > 0:
                            if rope_head[i] > rope_tail[i]:
                                delta_tail = (0, 1) if i else (1, 0)
                            else:
                                delta_tail = (0, -1) if i else (-1, 0)
                            rope_tail = tuple(map(add, rope_tail, delta_tail))
                    print(rope_tail)
                    visited.add(rope_tail)

    for y in range(10, -1, -1):
        line = ""
        for x in range(10):
            if (x, y) in visited:
                if (x, y) == (0, 0):
                    line += "s"
                else:
                    line += "x"
            else:
                line += "."
        print(line)

    part1 = len(visited)

    visited = {(0, 0)}  # already contains the start  - using a set as we only count each visited place once
    # - defaultdict and adding would also work! in case part2 requiries it :D

    ropes = [(0, 0)] * 10

    for line in input_lines:
        cur_dir, steps = line.split(" ")
        steps = int(steps)
        delta = DIRECTIONS[cur_dir]  # offset to current h_x, h_y
        for s in range(steps):
            # only move the first knot
            ropes[0] = tuple(map(add, ropes[0], delta))

            for j in range(1, len(ropes)):
                rope_head = ropes[j - 1]
                rope_tail = ropes[j]
                # check if we need to move:
                while max(abs(rope_tail[0] - rope_head[0]), abs(rope_tail[1] - rope_head[1])) > 1:
                    for i in range(2):
                        if abs(rope_tail[i] - rope_head[i]) > 0:
                            if rope_head[i] > rope_tail[i]:
                                delta_tail = (0, 1) if i else (1, 0)
                            else:
                                delta_tail = (0, -1) if i else (-1, 0)
                            rope_tail = tuple(map(add, rope_tail, delta_tail))
                ropes[j] = rope_tail
            # we only care about the last rope
            visited.add(ropes[-1])

    part2 = len(visited)


    for y in range(20, -20, -1):
        line = ""
        for x in range(-20,20):
            if (x, y) in visited:
                if (x, y) == (0, 0):
                    line += "s"
                else:
                    line += "x"
            else:
                line += "."
        print(line)


    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
