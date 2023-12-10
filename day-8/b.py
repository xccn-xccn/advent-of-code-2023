from sys import argv
from time import perf_counter

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


def main():
    text = read_file(get_input_file()).splitlines()

    grid = {}
    comm = {"L": 0, "R": 1}
    for line in text[2:]:
        start, end1, end2 = line[:3], line[7:10], line[12:15]
        # print(start, end1, end2)
        grid[start] = [end1, end2]


    currents = [x for x in grid if x[-1] == "A"]
    count = 0
    while any(square[-1] != "Z" for square in currents):
        # print(currents, count)
        for command in text[0]:
            for i, square in enumerate(currents):
                currents[i] = grid[square][comm[command]]
            count += 1

    return count

if __name__ == "__main__":
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')
