import sys
from collections import Counter

if __name__ == "__main__":
    with open(sys.argv[1], "r") as input_file:

        calories = Counter()
        i = 1
        for line in input_file:
            line = line.strip()
            if len(line) == 0:
                i += 1
            else:
                calories[i] += int(line)

    part1 = calories.most_common(1)[0][1]
    print(f"Part 1: {part1}")
    part2 = sum([y for x,y in calories.most_common(3)])
    print(f"Part 2: {part2}")