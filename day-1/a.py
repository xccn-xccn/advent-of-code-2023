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

def first_num(string, reverse=False):
    num = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    words = []
    # print(string)
    for c in string:

        if reverse:
            words = [c + x for x in words]
        else:
            words = [x + c for x in words]
        words.append(c)

        
        if c.isdigit():
            return c
        for w in words:
            if w in num:
                return num[w]

def main():
    num = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    text = read_file(get_input_file())
    # print(text, "\n")

    numbers = []
    for line in text.splitlines():
        numbers.append(int(first_num(line) + first_num(line[::-1], reverse=True)))
    
    return sum(numbers)



if __name__ == "__main__":
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')
