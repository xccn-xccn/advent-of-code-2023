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


def possible(line):
    most = {"red": 12, "green": 13, "blue": 14}

    # print(line[::2], line[1:2])
    for n, colour in zip(line[::2], line[1::2]):
        # print(n, colour)
        if not colour[-1].isalpha():
            colour = colour[:-1]

        if int(n) > most[colour]:
            return False
    
    # print("returning true")
    return True 

def main():
    text = read_file(get_input_file())
    score = 0
    for i, line in enumerate(text.splitlines(), 1):
        # line = line[7::]
        for index, c in enumerate(line):
            if c == ":":
                line = line[index+1:]
                # print(line)
                break

        line = line.split()
        if possible(line):
            # print("possible", line)
            score += i

    return score
            




if __name__ == "__main__":
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')
