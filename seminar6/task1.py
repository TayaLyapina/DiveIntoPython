# Задача 1.
# Вспомните какие модули вы уже проходили на курсе. 
# Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).

from random import randint as ri
from random import randrange as rr
from random import sample as s
from random import shuffle as sh

print(ri(1, 60))
print(rr(1, 60, 2))
data = [1, 8, 14, 9, 12, 18]
print(s(data, 6))
sh(data)
print(data)
