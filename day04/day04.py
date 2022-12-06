import sys

if __name__ == "__main__":
    with open(sys.argv[1], "r") as input_file:
        subsets = []  # s = []
        overlap = []
        for line in input_file:
            one, two = [v.split("-") for v in line.strip().split(",")]
            seq_one = range(int(one[0]), (int(one[1])+1))
            seq_two = range(int(two[0]), int(two[1])+1)
            set_one = set(seq_one)
            set_two = set(seq_two)
            subsets.append(set_one.issubset(set_two) or set_two.issubset(set_one))
            overlap.append(not set_one.isdisjoint(set_two))
    part1 = sum(subsets) #part_1(gamelines)

    part2 = sum(overlap) #part_2(gamelines)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
