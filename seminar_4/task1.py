# Задача 1.
# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.


def my_func(s: str) -> str:
    lst = s.split()
    m_l = len(max(lst))
    lst = sorted(lst)
    for i, el in enumerate(lst, 1):
        print(i, el.rjust(m_l))


print(my_func(input('Введите строку: ')))