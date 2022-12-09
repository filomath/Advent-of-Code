# ------- Advent of Code 2022 -------
# ------- Day 4: Camp Cleanup -------
# https://adventofcode.com/2022/day/4

def get_assignments(path_to_file):
    # loads assignment pairs "a-b,c-d" to a list of lists [a,b,c,d]
    with open(path_to_file) as file:
        lines = [line.split(",") for line in file.read().strip().split("\n")]
    pairs = [[int(a), int(b), int(c), int(d)] for a, b, c, d in [x.split("-") + y.split("-") for x, y in lines]]
    return pairs

if __name__ == "__main__":
    assignments = get_assignments("input.txt")
    print(sum([(a-c)*(b-d) <= 0 for a, b, c, d in assignments])) # Part One
    print(sum([(c<=a and a<=d) or (c<=b and b<=d) or (a<=c and c<=b) for a, b, c, d in assignments])) # Part Two