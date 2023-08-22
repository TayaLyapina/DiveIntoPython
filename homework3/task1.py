# Задача 1.
# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

lst = [1, 2, 5, 8, 2, 11, 3, 8, 1, 24, 7, 16, 10, 11]

count_dict = {}
for item in lst:
    count_dict[item] = count_dict.get(item, 0) + 1
repeat_elems = [key for key in count_dict.keys() if count_dict[key] > 1]
print(repeat_elems)

# Другой вариант выполнения задания

rep_elem = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j] and lst[i] not in rep_elem:
            rep_elem.append(lst[i])
print(rep_elem)