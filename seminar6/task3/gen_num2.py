from random import randint
from sys import argv

def guess_num(args):
    num = randint(args[0], args[1])
    i = 0
    while args[2] > i:
        u_num = int(input(f'введите число в диапазоне от {args[0]} до {args[1]}: '))
        if u_num > num:
            print('меньше')
        elif u_num < num:
            print('больше')
        else:
            print('угадал')
            return True
        i += 1
    return False


args = [int(el) for el in argv[1:]]
print(guess_num(args))