# ------- Advent of Code 2021 -------
# ----- Day 1: Calorie Counting -----
# https://adventofcode.com/2022/day/1

def get_calories(path_to_file): 
    # loads sums of calories carried by each elf to a list
    with open(path_to_file) as file:
        elves = file.read().strip().split("\n\n")
    return [sum(map(int, elf.split("\n"))) for elf in elves]
        
def top3(data): 
    # returns top 3 largest numbers in the list
    top3 = []
    for i in range(3):
        top3.append(max(data))
        data.remove(top3[i])
    return top3

if __name__ == "__main__":
    calories = get_calories("input.txt") 
    print(max(calories)) # Part One
    print(sum(top3(calories))) # Part Two