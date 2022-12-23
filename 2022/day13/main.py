# -------- Advent of Code 2022 --------
# ------ Day 13: Distress Signal ------
#  https://adventofcode.com/2022/day/13

from functools import cmp_to_key

def get_packets(path_to_file):
    # loads pairs of packets from given file to a list
    with open(path_to_file) as file:
        packets = [[eval(packet) for packet in pair.split("\n")] for pair in file.read().strip().split("\n\n")]
    return packets

def compare(left_item, right_item):
    # compares two packets given in form of list and determines whether they are in the right order
    if type(left_item) == list and type(right_item) == list:
        if left_item == []: return True
        if right_item == []: return False
        length = min(len(left_item), len(right_item))
        for i in range(length):
            if left_item[i] != right_item[i]:
                return compare(left_item[i], right_item[i])
        return len(left_item) < len(right_item)
    elif type(left_item) == int and type(right_item) == int:
        return left_item < right_item
    elif type(left_item) == int:
        return compare([left_item], right_item)
    elif type(right_item) == int:
        return compare(left_item, [right_item])

if __name__ == "__main__":
    pairs = get_packets("input.txt")
    print(sum(pairs.index(pair)+1 for pair in pairs if compare(pair[0], pair[1]))) # Part One
    packets = sorted(sum(pairs, []) + [[[2]], [[6]]], key=cmp_to_key(lambda x,y: 2*compare(x,y)-1), reverse=True)
    print((packets.index([[2]])+1) * (packets.index([[6]])+1)) # Part Two