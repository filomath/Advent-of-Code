# ------- Advent of Code 2022 -------
# ------- Day 5: Supply Stacks ------
# https://adventofcode.com/2022/day/5

import re

def get_cargo(path_to_file):
    # loads crates contents in stacks and instructions to move them in moves
    with open(path_to_file) as file:
        lines = []
        while True:
            line = file.readline().strip("\n")
            if line == "": break
            lines.append(line)
        moves = []
        while True:
            line = file.readline().strip("move \n")
            if line == "": break
            moves.append([int(x)-1 for x in re.split(" from | to ", line)])
    length = int(lines[-1].strip().split("   ")[-1])
    stacks = [""] * length
    for line in lines[:-1]:
        for i in range(length):
            stacks[i] += line[4*i+1].strip()
    return stacks, moves

def rearrangement(stacks, moves, part):
    # rearranges stacks according to moves and returns a string of top characters
    order = (-1) ** part
    for move in moves:
        stacks[move[2]] = stacks[move[1]][0:move[0]+1][::order] + stacks[move[2]]
        stacks[move[1]] = stacks[move[1]][move[0]+1:]
    return("".join([stack[0] for stack in stacks]))

if __name__ == "__main__":
    cargo = get_cargo("input.txt")
    print(rearrangement(cargo[0], cargo[1], 1)) # Part One
    cargo = get_cargo("input.txt")
    print(rearrangement(cargo[0], cargo[1], 2)) # Part Two