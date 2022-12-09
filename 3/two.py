from collections import defaultdict
from heapq import nlargest


def main():

    def priority(item :str):
        if item.islower():
            return ord(item) - 96
        return ord(item) - 38

    with open('3/input.txt') as f:
        text = f.read()
    
    rucksacks = text.split('\n')

    badges = []
    for group in range(0, len(rucksacks), 3):
        for item1 in rucksacks[group]:
            if item1 in rucksacks[group+1] and item1 in rucksacks[group+2]:
                badges.append(item1)
                break
    
    print(len(badges))
    print(sum([*map(priority, badges)]))



if __name__ == '__main__':
    main()