# -------- Advent of Code 2022 --------
# -- Day 12: Hill Climbing Algorithm --
#  https://adventofcode.com/2022/day/12

def get_heightmap(path_to_file):
    # loads the heightmap from a file to a list of rows of chars
    with open(path_to_file) as file:
        heightmap = [list(line) for line in file.read().strip().split("\n")]
    return heightmap

def find_char(heightmap, char):
    # finds coordinates of given char in the heightmap
    coordinates = []
    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            if heightmap[i][j] == char: 
                coordinates.append([i, j])
    return coordinates

def order(char):
    # assigns order to chars treating 'S' as 'a' and 'E' as 'z' 
    if char == 'S':
        return ord('a')
    elif char == 'E': 
        return ord('z')
    else: 
        return ord(char)

def find_path(heightmap, start, end_char, dir):
    # finds the shortest path between starting position and the nearest square containing end_char 
    # using BFS algorithm and returns its length, dir is 1 meaning upward or -1 meaning downward
    queue = [start]
    visited = [start]
    lengths = [0]
    while queue:
        square = queue.pop(0)
        for i, j in [[-1,0],[1,0],[0,-1],[0,1]]:
            neighbour = [square[0]+i, square[1]+j]
            if (0 <= neighbour[0] < len(heightmap) and 
                0 <= neighbour[1] < len(heightmap[0]) and 
                neighbour not in visited and 
                dir * (order(heightmap[neighbour[0]][neighbour[1]]) - order(heightmap[square[0]][square[1]])) < 2):
                visited.append(neighbour)
                lengths.append(lengths[visited.index(square)]+1)
                if heightmap[neighbour[0]][neighbour[1]] == end_char:
                    return lengths[-1]
                queue.append(neighbour)
    return 0

if __name__ == "__main__":
    heightmap = get_heightmap("input.txt")
    position, = find_char(heightmap, 'S')
    print(find_path(heightmap, position, 'E', 1)) # Part One
    position, = find_char(heightmap, 'E')
    print(find_path(heightmap, position, 'a', -1)) # Part Two