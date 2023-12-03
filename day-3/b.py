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
    gears = [] #char / number, (coords)
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

            if char == "*":
                gears.append((y, x))
        if num[0]:
            numbers.append(num)
    
    # print(gears)
    final_gears = []
    for coord in gears:
        final_gears.append(set())
        for dy, dx in ((-1, -1), (0, -1), (-1, 0), (0, 0), (1, -1), (-1, 1), (1, 0), (0, 1), (1, 1)):
            py, px = coord[0] + dy, coord[1] + dx

            final_gears[-1].add((py, px))

    # print(final_gears)
    # print(numbers)
    p_num = []
    for g_coords in final_gears:
        p_num = []
        for num, n_coord in numbers:
            if any(x in g_coords for x in n_coord):
                p_num.append(int(num))

                if len(p_num) == 2:
                    score += p_num[0] * p_num[1]
                    break
    return score




if __name__ == "__main__":
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')
