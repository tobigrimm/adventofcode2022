import copy
import sys
from itertools import islice
from collections.abc import Iterable
from typing import Tuple
import networkx
from operator import add, mul
from collections import deque
import math


class Monkey:
    def __init__(
        self,
        nr: int,
        startitems: list[int],
        op_string,
        test_function,
        monkey_if_true: int,
        monkey_if_false: int,
    ):
        self.nr = nr
        self.items = deque(startitems)
        self.op = lambda old: eval(op_string)
        self.test_value = test_value
        self.true_monkey = monkey_if_true
        self.false_monkey = monkey_if_false
        self.inspection_count = 0

    def calculate(self, worry_reducer=None):
        throw_item_list = []
        for item in self.items:
            self.inspection_count += 1
            worry_level = self.op(item)
            if worry_reducer is None:
                worry_level //= 3
            else:
                worry_level %= worry_reducer
            if worry_level % self.test_value == 0:
                throw_item_list.append((self.true_monkey, worry_level))
            else:
                throw_item_list.append((self.false_monkey, worry_level))
        self.items.clear()
        return throw_item_list


def calc_monkey_business(monkeys, worry_reducer: int | None = None):
    for r in range(1, 21 if worry_reducer is None else 10001):
        for monkey in monkeys:
            throw_list = monkey.calculate(worry_reducer)
            for new_monkey, item in throw_list:
                monkeys[new_monkey].items.append(item)

        # if r % 100 == 0:
        #    print(r)
        # if r == 1 or round == 20 or round == 1000:
        #    print(f"Round {r}")
        #    for monkey in monkeys:
        #        print(f"Monkey {monkey.nr} - Queue: {monkey.inspection_count}")
    foo = sorted([monkey.inspection_count for monkey in monkeys], reverse=True)
    return foo[0] * foo[1]


if __name__ == "__main__":
    monkeys = []
    with open(sys.argv[1], "r") as input_file:
        input_lines = input_file.read().splitlines()
        input_lines = [line.strip() for line in input_lines if len(line) > 0]
        for nr in range(len(input_lines) // 6):
            monkey_nr = int(input_lines[nr * 6][-2])
            assert nr == monkey_nr
            startitems = [
                int(item)
                for item in input_lines[(nr * 6) + 1].split(":")[1].strip().split(", ")
            ]
            op_string = input_lines[(nr * 6) + 2].split("=")[1].strip()
            op_func = lambda old: eval(op_string)
            test_value = int(input_lines[nr * 6 + 3].split("divisible by")[1].strip())
            true_monkey = int(input_lines[nr * 6 + 4].split("monkey")[1].strip())
            false_monkey = int(input_lines[nr * 6 + 5].split("monkey")[1].strip())

            monkeys.append(
                Monkey(
                    monkey_nr,
                    startitems,
                    op_string,
                    test_value,
                    true_monkey,
                    false_monkey,
                )
            )

    print(f" Part 1: {calc_monkey_business(copy.deepcopy(monkeys))}")

    # sys.exit()

    # it's all a ring!!!1! -  lowest common divisor is simply the product of all divisors as all divisors (test values) are prime
    worry_reducer = math.prod(monkey.test_value for monkey in monkeys)
    print(f" Part 2: {calc_monkey_business(monkeys, worry_reducer)}")
