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


def difference(*sequence):
    diff = []
    for num1, num2 in zip(sequence, sequence[1:]):
        diff.append(num2-num1)

    # print(diff, "diff")
    if all(x == 0 for x in diff):
        return sequence[-1] + diff[-1]
    
    x = difference(*diff)

    # print(x, sequence, "a")

    return sequence[-1] + difference(*diff)
    # return sequence[-1] + difference(*diff)

def main():
    text = read_file(get_input_file()).splitlines()
    score = 0

    for line in text:
        sequence = [int(x) for x in line.split()]
        # print(sequence, "sequence")
        value = difference(*sequence)

        # print(value)
        score += value

    return score

if __name__ == "__main__":
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')
