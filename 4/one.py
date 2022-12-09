from collections import defaultdict
from heapq import nlargest


def main():

    def range_conculsion(range_out, range_in):
        if range_out[0] <= range_in[0] and range_out[1] >= range_in[1]:
            return True
        return False

    def range_overlap(range_1, range_2):
        if (range_1[0] <= range_2[1] and range_1[1] >= range_2[0]):
            return True
        return False

    with open('4/input.txt') as f:
        text = f.read()

    data = [[[int(num) for num in elf_sec.split('-')] for elf_sec in line.split(',')] for line in text.split("\n")]
    counter = 0

    for pair in data:
        # if range_conculsion(pair[0], pair[1]) or range_conculsion(pair[1], pair[0]):
        if range_overlap(pair[0], pair[1]):
            counter += 1
    print(len(data))
    print(counter)

if __name__ == '__main__':
    main()