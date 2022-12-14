# ------- Advent of Code 2022 -------
# ---- Day 8: Treetop Tree House ----
# https://adventofcode.com/2022/day/8

def get_trees(path_to_file):
    # loads tree heights to a list
    with open(path_to_file) as file:
        trees = [[*line] for line in file.read().strip("\n").split("\n")]
    return trees

def viewing_distances(grid, i, j):
    # returns viewing distances from up, down, left and right of the tree in row i and column j in the grid
    # returns also a variable "visible" that says whether this tree is visible from outside the grid or not
    length = len(grid)
    visible = False
    up, down, left, right = 0, 0, 0, 0
    for k in [i-l-1 for l in range(i)]:
        up += 1
        if grid[k][j] >= grid[i][j]: break
        elif k == 0: visible = True
    for k in range(i+1, length):
        down += 1
        if grid[k][j] >= grid[i][j]: break
        elif k == length-1: visible = True
    for k in [j-l-1 for l in range(j)]:
        left += 1
        if grid[i][k] >= grid[i][j]: break
        elif k == 0: visible = True
    for k in range(j+1, length):
        right += 1
        if grid[i][k] >= grid[i][j]: break
        elif k == length-1: visible = True
    if i == 0 or i == length-1 or j == 0 or j == length-1: visible = True
    return up, down, left, right, visible

if __name__ == "__main__":
    grid = get_trees("input.txt")
    length = len(grid)
    visible_trees = 0
    max_score = 0
    for i in range(length):
        for j in range(length):
            dist = viewing_distances(grid, i, j)
            if dist[4]: visible_trees += 1
            new_score = dist[0] * dist[1] * dist[2] * dist[3]
            if new_score > max_score: max_score = new_score
    print(visible_trees) # Part One
    print(max_score) # Part Two