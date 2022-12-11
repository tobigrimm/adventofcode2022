import sys
from itertools import islice
from collections.abc import Iterable
from typing import Tuple
import networkx
from operator import add, mul
from collections import defaultdict
import queue

class Monkey:
    def __init__(self, nr: int, startitems: list[int], op_string, test_function, monkey_if_true: int, monkey_if_false: int):
        self.nr = nr
        self.items = queue.Queue()
        for item in startitems:
            self.items.put(item)
        self.op = lambda old: eval(op_string)
        self.test_value = test_value
        self.true_monkey = monkey_if_true
        self.false_monkey = monkey_if_false
        self.inspection_count = 0

    def calculate(self):
        throw_item_list = []
        while not self.items.empty():
            item = self.items.get()
            self.inspection_count += 1
            worry_level = self.op(item) // 3
            if worry_level % self.test_value == 0:
                throw_item_list.append((self.true_monkey, worry_level))
            else:
                throw_item_list.append((self.false_monkey, worry_level))

        return throw_item_list



if __name__ == "__main__":
    monkeys = []
    with open(sys.argv[1], "r") as input_file:
        input_lines = input_file.read().splitlines()
        input_lines = [line.strip() for line in input_lines if len(line) > 0]
        for nr in range(len(input_lines)//6):
            monkey_nr = int(input_lines[nr*6][-2])
            assert(nr == monkey_nr)
            startitems = [int(item) for item in input_lines[(nr*6)+1].split(":")[1].strip().split(", ")]
            op_string = input_lines[(nr*6)+2].split("=")[1].strip()
            op_func = lambda old: eval(op_string)
            test_value = int(input_lines[nr*6+3].split("divisible by")[1].strip())
            true_monkey = int(input_lines[nr*6+4].split("monkey")[1].strip())
            false_monkey = int(input_lines[nr*6+5].split("monkey")[1].strip())

            monkeys.append(Monkey(monkey_nr, startitems, op_string, test_value, true_monkey, false_monkey))





    for r in range(1,21):
        for monkey in monkeys:
            throw_list = monkey.calculate()
            for new_monkey, item in throw_list:
                monkeys[new_monkey].items.put(item)

        print(f"Round {r}")
        for monkey in monkeys:
            print(f"Monkey {monkey.nr} - Queue: {monkey.items.queue}")
    for monkey in monkeys:
        print(monkey.nr, monkey.inspection_count)

    part1 = 0
    print(f"Part 1: {part1}")
