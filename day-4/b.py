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


    instances = [1 for _ in range(len(text))]
    
    for g, game in enumerate(text):
        # print(game)
        for i, char in enumerate(game):
            if char == ":":
                game = game[i + 1:]

        card_count = instances[g]
        win, have = game.split("|")
        win, have = win.split(), have.split()
        count = 0
        # print(win, have)
        for num in have:
            if num in win:
                # print(num, "in", win)
                count += 1
        # print(count)

        for n in range(1, count + 1):
            instances[g + n] += card_count
    return sum(instances)


if __name__ == "__main__":
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')

# 10212704