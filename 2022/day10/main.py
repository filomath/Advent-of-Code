# -------- Advent of Code 2022 --------
# ----- Day 10: Cathode-Ray Tube ------
#  https://adventofcode.com/2022/day/10

def get_instructions(path_to_file):
    # loads CPU instructions to a list in the form of [increase of X, number of cycles]
    with open(path_to_file) as file:
        lines = file.read().strip().split("\n")
    instructions = []
    for line in lines:
        if line == "noop": instructions.append([0,1])
        else: instructions.append([int(line.split(" ")[-1]), 2])
    return instructions

def execution(instructions):
    # executes the program given by instructions and returns list of X values during consecutive cycles
    register_values = [0, 1] # i-th X value during i-th cycle
    for line in instructions:
        register_values.append(register_values[-1])
        if line[1] == 2: register_values.append(register_values[-1] + line[0])
    return register_values

def draw(register_values):
    # renders an image in the style of CRT
    CRT_output = ""
    for cycle in range(0,40):
        if abs(register_values[cycle] - cycle) < 2: CRT_output += "#"
        else: CRT_output += "."
    print(CRT_output)

if __name__ == "__main__":
    instructions = get_instructions("input.txt")
    register_values = execution(instructions)
    print(sum(number * register_values[number] for number in [20, 60, 100, 140, 180, 220])) # Part One
    for i in range(6): draw(register_values[40*i+1:40*(i+1)+1]) # Part Two