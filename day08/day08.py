import sys
from itertools import islice
from collections.abc import Iterable
from typing import Tuple
import networkx
from operator import add, mul





if __name__ == "__main__":
    with open(sys.argv[1], "r") as input_file:
        input_lines = input_file.read().splitlines()
        grid = {}
        max_x = len(input_lines[0])
        max_y = len(input_lines)
        for y, line in enumerate(input_lines):
            for x, tree in enumerate(line.strip()):
                grid[(x, y)] = int(tree)

        visible_trees = []
        part1 = 0
        UP = (0, -1)
        DOWN = (0, 1)
        LEFT = (-1, 0)
        RIGHT = (1, 0)
        DIRECTIONS = [UP, DOWN, LEFT, RIGHT]
        for x in range(0, max_x):
            for y in range(0, max_y):
                cur_tree = grid[(x, y)]
                if x == 0 or y == 0 or x == max_x - 1 or y == max_y - 1:
                    part1 += 1
                    visible_trees.append((x,y))
                else:
                    for direction in DIRECTIONS:
                        check_coord = (x, y)
                        while 0 < check_coord[0] < max_x - 1 and  0 < check_coord[1] < max_y - 1:
                            check_coord = tuple(map(add, check_coord, direction))
                            visible = False

                            # stop checking visibility in this direction if there is a higher tree
                            if cur_value := grid[check_coord] >= cur_tree:
                                break
                            else:
                                visible = True

                        # if a tree is visible in one direction, we can stop looking and move to the next
                        if visible:
                            part1 += 1
                            visible_trees.append((x, y))
                            break

    #for y in range(5):
    #    line = ""
    #    for x in range(5):
    #        #if (x, y) in visible_trees:
    #        line += str(grid[(x, y)])
    #    print(line)

    #print(" ---  ")

    #for y in range(5):
    #    line = ""
    #    for x in range(5):
    #        if (x,y) in visible_trees:
    #            line += str(grid[(x,y)])
    #        else:
    #            line += " "
    #    print(line)
    part2 = 0
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
