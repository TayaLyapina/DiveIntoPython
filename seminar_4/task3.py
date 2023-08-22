# Задача 3.
# Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def my_func(s: str, my_dict=None):
    if my_dict is None:
        my_dict = {}
    lst = s.split()
    lst = [int(x) for x in lst]
    for i in range(min(lst), max(lst) + 1):
        my_dict[chr(i)] = i
    return my_dict

nums = input('Введите два числа через пробел: ')
print(my_func(nums))