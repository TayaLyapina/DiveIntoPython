# Задача 1.
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

number = int(input("Введите число: "))
n = ''
DIVIDER = 16
print(hex(number))
while number > 0:
    add_num = str(number % DIVIDER)
    if add_num == '10':
        add_num = 'a' 
    elif add_num == '11':
        add_num = 'b'
    elif add_num == '12':
        add_num = 'c'
    elif add_num == '13':
        add_num = 'd'
    elif add_num == '14':
        add_num = 'e'
    elif add_num == '15':
        add_num = 'f'

    n = add_num + n
    number = number // DIVIDER
print(n)