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
    strength = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}
    hand = line.split()[0]

    counter_hand = Counter(hand)
    j_count = counter_hand["J"]
    counter_hand["J"], counter_hand["HOLD"] = 0, 0
    order = [x[1] for x in counter_hand.most_common(2)]


    order[0] += j_count

    f_hand = [strength.get(x, x) for x in hand]
    f_hand = [int(y) for y in f_hand]
    order.append(f_hand)

    return tuple(order)
def main():
    text = read_file(get_input_file()).splitlines()

    ordered = sorted(text, key = order_by)

    score = 0
    for i, line in enumerate(ordered, 1):
        score += int(line.split()[1]) * i
            
    return score
    
if __name__ == "__main__":
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')
