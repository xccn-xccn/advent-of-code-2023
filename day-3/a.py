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
    text = read_file(get_input_file())
    specials = set() 
    numbers = []
    score = 0

    for y, line in enumerate(text.splitlines()):
        num = ["", []]
        for x, char in enumerate(line):

            if char.isdigit():
                num[0] += char
                num[1].append((y, x))
            else:
                if num[0]:
                    numbers.append(num)
                num = ["", []]

            if not char.isalnum() and char != ".":
                specials.add((y, x))
        if num[0]:
            numbers.append(num)
    
    final_specials = set()
    for coord in specials:
        for dy, dx in ((-1, -1), (0, -1), (-1, 0), (0, 0), (1, -1), (-1, 1), (1, 0), (0, 1), (1, 1)):
            py, px = coord[0] + dy, coord[1] + dx

            final_specials.add((py, px))

    for num, coords in numbers:
        if any(x in final_specials for x in coords):
            score += int(num)

    return score




if __name__ == "__main__":
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')
