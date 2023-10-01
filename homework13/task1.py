# Задание
# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

class InvalidMatrixError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f'Все строки матрицы {self.data} должны иметь одинаковую длину'


class MatrixAdditionError(Exception):
    def __init__(self, message='Для сложения размеры матриц должны совпадать'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class MatrixMultiplicationError(Exception):
    def __init__(self, message='Для умножения количество столбцов первой матрицы должно быть равно количеству строк второй матрицы'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class Matrix:
    '''Class for working with matrix.
    Shows the operation of the help(cls) and the dander method __doc__'''

    def __init__(self, data):
        if len(set(len(row) for row in data)) != 1:
            raise InvalidMatrixError(data)
        self.data = data

    def __str__(self) -> str:
        '''Printing a class instance using the __str__ method'''
        data_str = "\n".join(["\t".join(map(str, row)) for row in self.data])
        return f'''Экземпляр класса Matrix содержит матрицу:
{data_str}'''

    def __repr__(self) -> str:
        '''Printing a class instance using the __repr__ method'''
        return f'Matrix({self.data})'

    def __eq__(self, other):  
        '''Comparing two matrices for equality'''
        return self.data == other.data

    def __ne__(self, other): 
        '''Comparing two matrices for inequality'''
        return self.data != other.data
    
    def __gt__(self, other):  # больше >
        '''Comparing two matrices: one is greater to the other'''
        return self.data > other.data

    def __ge__(self, other):  # больше или равно >=
        '''Comparing two matrices: one is greater or equal to the other'''
        return self.data >= other.data

    def __lt__(self, other):  # метод меньше <
        '''Comparing two matrices: one is less to the other'''
        return self.data < other.data

    def __le__(self, other):  # меньше или равно <=
        '''Comparing two matrices: one is less or equel to the other'''
        return self.data <= other.data

    def __add__(self, other):
        '''Addition of two matrices'''
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise MatrixAdditionError()

        result = [
            [self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ]
        return Matrix(result)

    def __mul__(self, other):
        '''Multiplying two matrices'''
        if len(self.data[0]) != len(other.data):
            raise MatrixMultiplicationError()

        result = [
            [sum(self.data[i][k] * other.data[k][j] for k in range(len(self.data[0])))for j in range(len(other.data[0]))]
            for i in range(len(self.data))
        ]
        return Matrix(result)
        

m1 = Matrix(([1, 2, 3], [1, 2, 3], [1, 2, 3]))
m2 = Matrix(([2, 2, 3], [3, 2, 3], [4, 2, 3]))
m3 = m1 + m2
print(m3)
m4 = m1 * m2
print(m4)