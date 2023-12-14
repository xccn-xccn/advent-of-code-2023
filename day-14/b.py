from sys import argv
from time import perf_counter

start = perf_counter()

#Check for repitition then mod to find the exact cycle you want
def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def get_input_file():
    if len(argv) == 1:
        return "sample.txt"
    elif len(argv) == 2:
        return argv[1] if argv[1] != "i" else "input.txt"


def main():
    text = read_file(get_input_file()).splitlines()

    fixed = [set() for _ in range(len(text))]
    rocks = [[] for _ in range(len(text))]

    score = 0
    length = len(text)
    for y, row in enumerate(text):
        for x, square in enumerate(row):
            if square == "O":
                rocks[x].append(y)
            elif square == "#":
                fixed[x].add(y)

    for c_fixed, c_rocks in zip(fixed, rocks):
        for rock in c_rocks:
            for y in range(rock, -1, -1):
                if y in c_fixed:
                    c_fixed.add(y + 1)
                    score += length - (y + 1)
                    break
                elif y == 0:
                    c_fixed.add(0)
                    score += length

    return score


if __name__ == "__main__":
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
