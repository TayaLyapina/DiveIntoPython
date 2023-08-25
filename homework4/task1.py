# Задача 1.
# Напишите функцию для транспонирования матрицы


def my_func(my_matrix):
    rows = len(my_matrix)
    cols = len(my_matrix[0])
    transp_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transp_matrix[j][i] = my_matrix[i][j]
    return transp_matrix


matrix = [[0, 1, 5], [1, 6, 9], [8, 2, 4]]
print(my_func(matrix))