from collections import Counter
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


def order_by(line):
    strength = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    hand = line.split()[0]
    order = [x[1] for x in Counter(hand).most_common(2)]

    f_hand = [strength.get(x, x) for x in hand]
    f_hand = [int(y) for y in f_hand]
    print(f_hand, hand)
    order.append(str(f_hand))

    return tuple(order)
def main():
    text = read_file(get_input_file()).splitlines()

    # text = [int(x), int(y) for x, y in line.split() for line in text]

    ordered = sorted(text, key = order_by)
    # for line in text:
    #     for hand, bid in line:
    #         hand, bid = int(hand), int(bid)

    print(ordered)
            
            
    
if __name__ == "__main__":
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')
