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


def double_blanks(text):
    grid = []
    for line in text:
        grid.append(line)

        if all(x == "." for x in line):
            grid.append(line)

    return grid
def main():
    text = read_file(get_input_file()).splitlines()

    grid = double_blanks(text)
    grid = double_blanks(zip(*grid))
    
    


if __name__ == "__main__":
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')
