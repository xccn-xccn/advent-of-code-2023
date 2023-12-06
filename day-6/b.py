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

    #formula  d = h * (t-h)
    for i, line in enumerate(text):
        for j, char in enumerate(line):
            if char == ":":
                text[i] = [int("".join(text[i][j + 1 :].split()))]

    result = 1
    for time, record in zip(text[0], text[1]):
        count = 0
        for h in range(1, time):
            d = h * (time - h)

            if d > record:
                count += 1

        result *= count

    return result

if __name__ == "__main__":
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
