# ------- Advent of Code 2022 -------
# ---- Day 2: Rock Paper Scissors ---
# https://adventofcode.com/2022/day/2

def get_strategy(path_to_file): 
    # loads strategies to a list with following encoding: rock=1, paper=2, scissors=3
    with open(path_to_file) as file:
        rounds = file.read().strip().split("\n")
    letters = ["A", "X", "B", "Y", "C", "Z"]
    return [list(map(lambda s: letters.index(s)//2+1, line.split(" "))) for line in rounds]

def total_score(strategy, part):
    # sums points for both choices and results with given strategy and interpreted as for part=1 or part=2
    if part == 1: 
        return sum(map(lambda x: x[1] + (x[1]-x[0]+1)%3*3, strategy))
    else:
        return sum(map(lambda x: (x[0]+x[1])%3+1 + (x[1]-1)*3, strategy))

if __name__ == "__main__":
    strategy = get_strategy("input.txt")
    print(total_score(strategy, 1)) # Part One
    print(total_score(strategy, 2)) # Part Two
