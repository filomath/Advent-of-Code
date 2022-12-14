# ------- Advent of Code 2022 -------
# -------- Day 9: Rope Bridge -------
# https://adventofcode.com/2022/day/9

def get_moves(path_to_file):
    # loads the list of head's moves in the form of [direction, number]
    with open(path_to_file) as file:
        moves = [move.split(" ") for move in file.read().strip().split("\n")]
    return moves

def head_move(head, direction):
    # this function returns position of head after one step of head in the given direction
    udrl = {"U":[0,1], "D":[0,-1], "R":[1,1], "L":[1,-1]} # letter to coord and its change
    head[udrl[direction][0]] += udrl[direction][1] 
    return head

def knot_move(head, tail):
    # this function returns position of tail given the position of moved head
    for i in [0,1]:
        if head[i] == tail[i]:
            if head[1-i] == tail[1-i]+2: tail[1-i] += 1
            elif head[1-i] == tail[1-i]-2: tail[1-i] -= 1
    if abs(tail[0] - head[0]) + abs(tail[1] - head[1]) > 2:
        tail[0] += int((head[0] - tail[0]) / abs(head[0] - tail[0]))
        tail[1] += int((head[1] - tail[1]) / abs(head[1] - tail[1]))
    return tail

def trajectory(positions, moves):
    # returns number of visited points by tail
    visited = {(0,0)}
    for move in moves:
        for i in range(int(move[1])):
            positions[0] = head_move(positions[0], move[0])
            for j in range(1,len(positions)):
                positions[j] = knot_move(positions[j-1], positions[j])
            visited.add(tuple(positions[-1]))
    return len(visited)

if __name__ == "__main__":
    moves = get_moves("input.txt")
    print(trajectory([[0,0] for i in range(2)], moves)) # Part One
    print(trajectory([[0,0] for i in range(10)], moves)) # Part Two