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


def convert_single(section, current):
    for line in section.splitlines()[1:]:
        line = [int(x) for x in line.split()]

        end, start, length = line
        
        # print(start, current, length, start + length)
        # print((start <= current < (start + length)))
        if start <= current < (start + length):
            # print("in")
            return end + current - start
        
    return current
def main():
    text = read_file(get_input_file())

    text = text.split("\n\n")
    # print(text)
    # keys = [{} for _ in range(len(text) - 1)]
    # for i, section in enumerate(text[1:]):
    #     for line in section.splitlines()[1:]:
    #         line = [int(x) for x in line.split()]

    #         end, start, length = line
    #         for d in range(length):
    #             # print("in d")
    #             keys[i][start + d] = end + d


    # print(keys)

    seeds = text[0]
    for i, char in enumerate(seeds):
            if char == ":":
                seeds = seeds[i + 1:]
        
    seeds = [int(x) for x in seeds.split()]

    # final_seeds = []
    # for start, arange in zip(seeds[::2], seeds[1::2]):
    #     for n in range(arange):
    #         final_seeds.append(start + n)
    # print(seeds)

    min_location = float("inf")
    for minimum, extra in zip(seeds[::2], seeds[1::2]):
        for value in range(minimum, minimum + extra):
            for section in (text[1:]):
                # print(seed)
                value = convert_single(section, value)
                # print(seed, section, "after convert")
            if value < min_location:
                min_location = value
    
        # end_val = value
        # for section in (text[:0:-1]):
        #     # print(value)
        #     value = convert_single(section, value)
        #     # print(value, section, "after convert")

        # if valid(value, seeds):
        #     return end_val

    return min_location
if __name__ == "__main__":
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
