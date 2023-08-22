# Задача 6.
# Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.


def sum_of_nums(lst: list[int], i_1, i_2):
    min_i = min(i_1, i_2)
    max_i = max(i_1, i_2)
    if min_i < 0:
        min_i = 0
    if max_i > len(lst):
        max_i = len(lst)
    addition = 0
    for i in range(min_i, max_i + 1):
        addition += lst[i]
    return addition


nums_lst = list(map(int, input('Введите список чисел через пробел: ').split()))
index_1, index_2 = map(int, input("Введите индексы начала и конца через пробел: ").split())
print(sum_of_nums(nums_lst, index_1, index_2))