import sys


def calc_char(c):
    val = ord(c)
    if val < 97:
        return val - 38
    else:
        return val - 96


def part_1(inputlines):
    sum = 0
    for line in inputlines:
        half_line = len(line) // 2  # this will give type int
        first = line[:half_line]
        second = line[half_line:]
        char = next(iter(set(first).intersection(set(second))))
        sum += calc_char(char)
    return sum


def chunks(lst, n):
    """Create n-sized chunked from given list lst """
    for i in range(0, len(lst), n):
        yield lst[i: i + n]


def part_2(inputlines):
    sum = 0
    grouped = chunks(inputlines, 3)
    for chunked_groups in grouped:
        initial_set = None
        # work on arbitrary chunk sizes
        for group in chunked_groups:
            if initial_set:
                intial_set = initial_set.intersection(set(group))
            else:
                initial_set = set(group)

        char = next(iter(initial_set))
        sum += calc_char(char)
    return sum


if __name__ == "__main__":
    with open(sys.argv[1], "r") as input_file:
        gamelines = []  # s = []
        for line in input_file:
            gamelines.append(line.strip())

    part1 = part_1(gamelines)

    part2 = part_2(gamelines)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
