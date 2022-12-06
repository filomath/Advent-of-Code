# ------- Advent of Code 2022 -------
# -- Day 3: Rucksack Reorganization -
# https://adventofcode.com/2022/day/3

def get_rucksacks(path_to_file): 
    # loads contents of rucksacks into a list of strings
    with open(path_to_file) as file:
        rucksacks = file.read().strip().split("\n")
    return rucksacks

def shared_types(rucksacks):
    # returns common elements among given rucksacks as a set
    shared = set(rucksacks[0])
    for rucksack in rucksacks:
        shared = shared.intersection(rucksack)
    return shared

def priorities(types):
    # sums priorities of types in a list
    a = ord('a')
    A = ord('A')
    priorities = {chr(i): i - a + 1 for i in range(a, a + 26)}
    priorities.update({chr(i): i - A + 27 for i in range(A, A + 26)})
    return sum([priorities[x] for x in types])

if __name__ == "__main__":
    rucksacks = get_rucksacks("input.txt")
    print(priorities([y for y, in [shared_types([r[:len(r)//2], r[len(r)//2:]]) for r in rucksacks]])) # Part One
    print(priorities([y for y, in [shared_types(rucksacks[i:i+3]) for i in range(0,len(rucksacks),3)]])) # Part Two
