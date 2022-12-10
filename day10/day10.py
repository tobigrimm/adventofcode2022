import sys
from itertools import islice
from collections.abc import Iterable
from typing import Tuple
import networkx
from operator import add, mul
from collections import defaultdict


class CPU:
    def __init__(self, instructions: list[str]):
        self.instructions = instructions
        self.IP = 0
        self.registers = defaultdict(lambda: 1)
        self.INSTRUCTIONS = {"addx": {"cycles": 2}, "noop": {"cycles": 1}}
        self.display = [""] * 6 * 40

    def execute(self):
        signal_cycles = list(range(20, 230, 40))

        signal_sum = 0

        clock_cycles = 1
        current_pixel = 0

        while 0 <= self.IP < len(self.instructions):

            next_ins, *params = self.instructions[self.IP].split(" ")
            remaining_cycles = self.INSTRUCTIONS[next_ins]["cycles"]
            while remaining_cycles > 0:
                # draw screen
                # sprite is 3 pixels wide
                if self.registers["X"] - 1 <= current_pixel <= self.registers["X"] + 1:
                    pixel = "#"
                else:
                    pixel = "."
                self.display[clock_cycles - 1] = pixel
                current_pixel += 1
                current_pixel = current_pixel % 40

                if clock_cycles in signal_cycles:
                    signal_sum += clock_cycles * self.registers["X"]

                if remaining_cycles == 1:
                    # execute instruction
                    if next_ins == "noop":
                        pass
                    elif next_ins == "addx":
                        self.registers["X"] += int(params[0])

                clock_cycles += 1
                remaining_cycles -= 1
                # print(f"clock: {clock_cycles} X: {self.registers['X']}")

            # grab next instruction, possible ending execution if its the last
            self.IP += 1

        return signal_sum


if __name__ == "__main__":
    with open(sys.argv[1], "r") as input_file:
        input_lines = input_file.read().splitlines()

    cpu = CPU(input_lines)
    part1 = cpu.execute()

    print(f"Part 1: {part1}")

    for y in range(6):
        line = ""
        for x in range(40):
            line += cpu.display[y * 40 + x]
        print(line)
