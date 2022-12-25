# -------- Advent of Code 2022 --------
# ---- Day 14: Regolith Reservoir -----
#  https://adventofcode.com/2022/day/14

import os

def get_rocks(path_to_file):
    # returns a list of coordinates of all rocks
    paths = []
    with open(path_to_file) as file:
        line = file.readline()
        while line:
            paths.append([list(eval(rock)) for rock in line.strip().split(" -> ")])
            line = file.readline()
    rocks = []
    for path in paths:
        start = path[0]
        rocks.append(start)
        for i in range(1, len(path)):
            end = path[i]
            if start[0] == end[0]:
                x = 0
                y = int((end[1]-start[1])/abs(end[1]-start[1]))
            else:
                x = int((end[0]-start[0])/abs(end[0]-start[0]))
                y = 0
            while True:
                rocks.append([rocks[-1][0]+x, rocks[-1][1]+y])
                if rocks[-1] == end: break
            start = path[i]
    return rocks

def add_sand_unit(rocks, sand):
    # simulates a falling sand unit and appends its final coordinates to given list
    # if the sand unit falls into the void, it returns False
    # if the sand unit comes to rest, it returns True
    sand_unit = [500, 0]
    obstacles = rocks + sand
    void = max(rock[1] for rock in rocks)
    while True:
        if [sand_unit[0], sand_unit[1]+1] not in obstacles:
            sand_unit = [sand_unit[0], sand_unit[1]+1]
        elif [sand_unit[0]-1, sand_unit[1]+1] not in obstacles:
            sand_unit = [sand_unit[0]-1, sand_unit[1]+1]
        elif [sand_unit[0]+1, sand_unit[1]+1] not in obstacles:
            sand_unit = [sand_unit[0]+1, sand_unit[1]+1]
        else: break
        if sand_unit[1] > void: return False
    sand.append(sand_unit)
    return True

def draw(rocks, sand):
    # draws rocks and sand in the terminal window (be sure to adjust its size and font to see the whole image)
    os.system("clear")
    for i in range(max(rock[1] for rock in rocks)+1):
        line = ""
        for j in range(min(rock[0] for rock in rocks), max(rock[0] for rock in rocks)+1):
            if [j, i] in rocks:
                line += "#"
            elif [j, i] in sand:
                line += "o"
            else:
                line += "."
        print(line)

if __name__ == "__main__":
    rocks = get_rocks("input.txt")
    sand = []
    while add_sand_unit(rocks, sand):
        continue
    print(len(sand)) # Part One
    M = max(rock[1] for rock in rocks)
    for i in range(500-M-5, 500+M+5):
        rocks.append([i, 2+M])
    while [500,0] not in sand:
        add_sand_unit(rocks, sand)
    print(len(sand)) # Part Two