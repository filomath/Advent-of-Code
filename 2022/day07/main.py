# ------- Advent of Code 2022 -------
# -- Day 7: No Space Left On Device -
# https://adventofcode.com/2022/day/7

def get_directories(path_to_file):
    # loads terminal outputs and returns a dictionary of directories and its sizes
    current_path = []
    directories = {}
    with open(path_to_file) as file:
        while True:
            line = file.readline().strip("\n")
            if line == "": break
            elif line.startswith("$ cd"):
                if line[5] == ".": 
                    current_path.pop()
                else: 
                    current_path.append(line[5:])
                    directories["".join(current_path)] = 0
            elif line[0] in {str(i) for i in range(10)}:
                for i in range(len(current_path)):
                    directories["".join(current_path[:i+1])] += int(line.split()[0])
    return directories

if __name__ == "__main__":
    directories = get_directories("input.txt")
    print(sum(directories[x] for x in directories if directories[x] <= 100000)) # Part One
    needed_space =  directories["/"] - 40000000
    print(min(directories[x] for x in directories if directories[x] >= needed_space)) # Part Two