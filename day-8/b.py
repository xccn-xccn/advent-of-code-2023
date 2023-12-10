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


def gcd(a, b):
    if a == 0 or b == 0:
        return a + b
    
    return gcd(b, a%b)

def lcm(a, b):
    return a * b / gcd(a, b)

def lcmm(*nums):
    if len(nums) == 1:
        return nums[0]
    
    return lcmm(lcm(nums[0], nums[1]) , *nums[2:])

def main():
    text = read_file(get_input_file()).splitlines()

    grid = {}
    comm = {"L": 0, "R": 1}
    for line in text[2:]:
        start, end1, end2 = line[:3], line[7:10], line[12:15]
        # print(start, end1, end2)
        grid[start] = [end1, end2]

    print("aa")

    currents = [x for x in grid if x[-1] == "A"]
    # counts = [0 for _ in grid]
    # count = 0
    # while 0 in counts:
    #     # print(currents, count)
    #     for command in text[0]:
    #         for i, square in enumerate(currents):
    #             currents[i] = grid[square][comm[command]]

    #             if currents[i][-1] == "Z":
    #                 counts[i] = count
    #         count += 1

    counts = []
    for i, square in enumerate(currents):
        count = 0
        while square[-1] != "Z":
            for command in text[0]:
                square = grid[square][comm[command]]
                count += 1

                if square[-1] == "Z":
                    counts.append(count)
                    break

    return lcmm(*counts)

if __name__ == "__main__":
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')
