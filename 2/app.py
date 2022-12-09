import numpy as np


payoff = np.array([[4, 8, 3],
                   [1, 5, 9],
                   [7, 2, 6]])

move_map = {'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2}

move_map_part_two = {'X': -1, 'Y': 0, 'Z': 1}

def play(opponent, me):
    if opponent not in ('A', 'B', 'C') or me not in ('X', 'Y', 'Z'):
        raise ValueError('Wrong input')

    return payoff[move_map[opponent], move_map[me]]

def play_part_two(opponent, me):
    if opponent not in ('A', 'B', 'C') or me not in ('X', 'Y', 'Z'):
        raise ValueError('Wrong input')

    return payoff[move_map[opponent], (move_map[opponent] + move_map_part_two[me])%3]

def main():
    with open('2/input.txt') as f:
        text = f.read()

    score = sum([play_part_two(*game.split(' ')) for game in text.split('\n')])
    print(score)

if __name__ == '__main__':
    main()