# Задача 2.
# Создайте модуль с функцией внутри. 
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток. 
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток. 
# Функция выводит подсказки “больше” и “меньше”. 
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.



import gen_num


result = gen_num.guess_the_num(1, 80, 6)
print(result)