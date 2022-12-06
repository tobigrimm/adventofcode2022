import sys
import copy
from collections import defaultdict


def crane(crane_moves, crane_stacks, crane_type="9000"):
    for crane_move in crane_moves:
        amount, source, target = crane_move
        if crane_type == "9001":
            crane_stacks[target].extend(move_crates := crane_stacks[source][-amount:])
            crane_stacks[source] = crane_stacks[source][:-amount]
        else:
            for i in range(amount):
                crane_stacks[target].extend(move_crates := crane_stacks[source][-1:])
                crane_stacks[source] = crane_stacks[source][:-1]
    return "".join([crane_stacks[i][-1] for i in range(1, stack_nr + 1)])


if __name__ == "__main__":
    with open(sys.argv[1], "r") as input_file:
        stacks = defaultdict(list)
        moves = []
        gamelines = []  # s = []
        read_stacks = True
        lines = input_file.readlines()
        stack_nr = 0
        # find number of stacks
        for line in lines:
            line = line.strip()
            if line.startswith('1'):
                stack_nr = int(line.split(" ")[-1])
        for line in lines:
            if line.startswith("move"):
                line = line.strip()
                move = line.split(" ")
                moves.append([int(move[1]), int(move[3]), int(move[5])])
            if "[" in line:

                for i in range(stack_nr):
                    c = i * 4
                    stack_append = line[c:c + 4].strip().replace('[', '').replace(']', '')
                    if len(stack_append) > 0:
                        stacks[i + 1].append(stack_append)

    # TODO reorder stacks!
    for i in stacks:
        stacks[i] = list(reversed(stacks[i]))

    part1 = crane(moves, copy.deepcopy(stacks))
    part2 = crane(moves, copy.deepcopy(stacks), "9001")

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
