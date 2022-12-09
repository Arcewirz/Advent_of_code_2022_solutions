from heapq import nlargest


def main():
    with open('2/input.txt') as f:
        text = f.read()

    total_cal_list = [sum([int(food_item) for food_item in cal_string.split('\n')]) 
                        for cal_string in text.split('\n\n')]
                        
    best_3 = nlargest(3, total_cal_list)
    print(best_3)
    print(sum(best_3))

if __name__ == '__main__':
    main()