import sys

"""First column: Opponent - A for Rock, B for Paper, and C for Scissors
   The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. 


   Your total score is the sum of your scores for each round. 
   The score for a single round is the score for the shape you selected 
   (1 for Rock, 2 for Paper, and 3 for Scissors) 
   plus the score for the outcome of the round 
   (0 if you lost, 3 if the round was a draw, and 6 if you won).

    Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.

"""


def calculate_round_part1(game_line) -> int:
    opp = game_line[0]
    myself = game_line[1]
    chosen_score = {"X": 1, "Y": 2, "Z": 3}

    wins = {"X": "C", "Z": "B", "Y": "A"}

    draw = {"A": "X", "B": "Y", "C": "Z"}

    if draw[opp] == myself:
        outcome_score = 3
    elif wins[myself] == opp:
        outcome_score = 6
    else:
        # we lost?
        outcome_score = 0
    return outcome_score + chosen_score[myself]


def calculate_round_part2(game_line) -> int:
    opp = game_line[0]
    goal = game_line[1]
    chosen_score = {"A": 1, "B": 2, "C": 3}
    outcome_score = {"X": 0, "Y": 3, "Z": 6}

    wins = {"A": "C", "C": "B", "B": "A"}
    lose = {v: k for k, v in wins.items()}

    if outcome_score[goal] == 0:
        # lose - opponent wins
        myself = wins[opp]
    elif outcome_score[goal] == 3:
        # draw, choose the same!
        myself = opp
    else:
        # I win! - opponent loses
        myself = lose[opp]

    return outcome_score[goal] + chosen_score[myself]


if __name__ == "__main__":
    sum = 0
    with open(sys.argv[1], "r") as input_file:
        gameline = "" #s = []
        for line in input_file:
            gameline = line.strip()
            l = len(gameline)
            first = gameline[:int(l/2)]
            second = gameline[int(l/2):]
            char = next(iter(set(first).intersection(set(second))))

            if(ord(char)<97):
                sum += ord(char)-38
            else:
                sum += ord(char)-96

part1 = sum

part2 = 0

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
