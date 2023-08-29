import random


def guess_the_num(lower_bound, upper_bound, attempts):

    number = random.randint(lower_bound, upper_bound)

    for _ in range(attempts):
        numb = int(input('Введите число: '))
        if number > numb:
            print('Загаданное число больше')
        elif number < numb:
            print('Загаданное число меньше')
        else:
            return True
        
    return False



