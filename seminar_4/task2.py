# Задача 2.
# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.


def my_func(s: str, data=None):
    if data is None:
        data = []
    lst = list(s)
    for el in lst:
        data.append(ord(el))
    return sorted(data)


print(my_func(input('Введите строку: ')))
