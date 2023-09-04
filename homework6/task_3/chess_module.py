'''Chess Module with Eight Queens Task, where a random number generator is used to arrange the queens'''
from random import randint as rnd


def eigth_queens(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True

def random_queens(num):
    count = 0
    len_queens = 8
    while count < num:
        queens = []
        for _ in range(len_queens):
            x = rnd(1, 8)
            y = rnd(1, 8)
            queens.append((x, y))

        if eigth_queens(queens):
            print(f"Успешная расстановка ферзей: {queens}")
            count += 1

