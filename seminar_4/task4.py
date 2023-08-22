# Задача 4.
# Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff
    return array


lst = [25, 45, 78, 85, 12, 48, 9, 16, 23, 14, 88, 10]
print(bubble_sort(lst))
