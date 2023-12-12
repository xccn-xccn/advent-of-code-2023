from sys import argv
from time import perf_counter
from collections import deque

start = perf_counter()
def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def get_input_file():
    if len(argv) == 1:
        return "sample.txt"
    elif len(argv) == 2:
        return argv[1] if argv[1] != "i" else "input.txt"


def double_blanks(text):
    grid = []
    for line in text:
        grid.append(line)

        if all(x == "." for x in line):
            grid.append(line)

    return grid

# def paths(grid, start):

#     bag = deque([start])

#     while True:
#         cy, cx = bag.popleft()
#         for dy, dx in ((0, 1), (1, 0)):
#             py, px = cy + dy, cx + dx



def main():
    text = list(map(list, read_file(get_input_file()).splitlines()))

    grid = double_blanks(text)
    grid = list(zip(*double_blanks(zip(*grid[::-1]))))[::-1] #rotate grid double blanks then rotate back
    
    galaxies = []
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "#":
                galaxies.append((y, x))

    score = 0
    count = 0
    for i, (y, x) in enumerate(galaxies):
        # print(i, y, x)
        for y2, x2 in galaxies[i+ 1:]:
            count += 1
            # print(i, b, y, x, y2, x2)
            score += abs(y2 - y) + abs(x2 - x)

    # print(count)
    return score


if __name__ == "__main__":
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')
