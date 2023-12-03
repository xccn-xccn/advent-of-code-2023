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


def get_most(line):
    most = {"red": 0, "green": 0, "blue": 0}

    # print(line[::2], line[1:2])
    for n, colour in zip(line[::2], line[1::2]):
        # print(n, colour)
        if not colour[-1].isalpha():
            colour = colour[:-1]

        most[colour] = max(most[colour], int(n))
    
    # print("returning true")
    return most 

def main():
    text = read_file(get_input_file())
    score = 0
    for i, line in enumerate(text.splitlines(), 1):
        # line = line[7::]
        for index, c in enumerate(line):
            if c == ":":
                line = line[index+1:]
                break

        line = line.split()
        
        power = 1
        for c in get_most(line).values():
            power *= c

        score += power
    return score
            




if __name__ == "__main__":
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')
