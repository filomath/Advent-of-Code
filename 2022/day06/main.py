# ------- Advent of Code 2022 -------
# ------ Day 6: Tuning Trouble ------
# https://adventofcode.com/2022/day/6

def get_buffer(path_to_file):
    # loads a buffer and returns it as string variable
    with open(path_to_file) as file:
        buffer = file.read().strip()
    return buffer

def find_marker(buffer, length):
    # returns index of the first character that forms a marker of given length
    i = length-1
    while len(set(buffer[i-length+1:i] + buffer[i])) < length: i += 1
    return i+1


if __name__ == "__main__":
    buffer = get_buffer("input.txt")
    print(find_marker(buffer, 4)) # Part One
    print(find_marker(buffer, 14)) # Part Two