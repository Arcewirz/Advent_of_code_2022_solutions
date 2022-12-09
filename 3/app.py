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

    rucksacks_comps = [(ruck[:len(ruck)//2], ruck[len(ruck)//2:]) for ruck in rucksacks]
    item_both_count = defaultdict(int)

    for comps in rucksacks_comps:
        for item in comps[0]:
            if item in comps[1]:
                item_both_count[item] += 1
                break
                

    

    # most_common = nlargest(1, item_both_count, key=item_both_count.get)[0]

    print(len(rucksacks_comps))
    print(sum([i for i in item_both_count.values()]))
    print(sum([priority(item)*count for item, count in item_both_count.items()]))
    # print(item_both_count[most_common]*priority(most_common))


if __name__ == '__main__':
    main()