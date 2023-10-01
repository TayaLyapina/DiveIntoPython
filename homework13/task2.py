class InvalidLengthError(Exception):
    def __init__(self, length):
        self.length = length

    def __str__(self):
        return f'Длина прямоугольника = {self.length}, а должна быть больше 0.'


class InvalidWigthError(Exception):
    def __init__(self, wigth):
        self.wigth = wigth

    def __str__(self):
        return f'Ширина прямоугольника = {self.wigth}, а должна быть больше 0.'


class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        if width is None:
            self.width = length
        else:
            self.width = width

    @property
    def width(self):
        return self._width
    
    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, new_len):
        if new_len <= 0:
            raise InvalidLengthError(new_len)
        self._length = new_len

    @width.setter
    def width(self, new_wid):
        if new_wid <= 0:
            raise InvalidWigthError(new_wid)
        self._width = new_wid

    def get_perimeter(self):
        return 2 * (self._width + self._length)

    def get_area(self):
        return self._width * self._length

    def __add__(self, other):
        res = self.get_perimeter() + other.get_perimeter()
        return Rectangle(res)

    def __sub__(self, other):
        res = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(res)

    def __eq__(self, other):  # равно ==
        return self.get_area() == other.get_area()

    def __ne__(self, other):  # неравно !=
        return self.get_area() != other.get_area()

    def __gt__(self, other):  # больше >
        return self.get_area() > other.get_area()

    def __ge__(self, other):  # больше или равно >=
        return self.get_area() >= other.get_area()

    def __lt__(self, other):  # метод меньше <
        return self.get_area() < other.get_area()

    def __le__(self, other):  # меньше или равно <=
        return self.get_area() <= other.get_area()

    def __str__(self) -> str:
        res = f'Прямоугольник со сторонами {self._width} и {self._length}'
        return res
    

r1 = Rectangle(7, 11)

print(r1)
r1.width = 11
print(r1)
r1.length = 11
print(r1)