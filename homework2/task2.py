# Задача 2.
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

import fractions

n_1, n_2 = map(int, input("Введите строку формата a/b: ").split("/"))
n_3, n_4 = map(int, input("Введите строку формата a/b: ").split("/"))

numerator = n_1 * n_4 + n_2 * n_3
denominator = n_2 * n_4
if denominator % numerator == 0:
    denominator = denominator // numerator
    numerator = 1 
print(f'Сумма дробей {n_1}/{n_2} и {n_3}/{n_4} равна {numerator}/{denominator}')

numerator = n_1 * n_3
denominator = n_2 * n_4
if denominator % numerator == 0:
    denominator = denominator // numerator
    numerator = 1
print(f'Произведение дробей {n_1}/{n_2} и {n_3}/{n_4} равно {numerator}/{denominator}')

print('Проверка')
f1 = fractions.Fraction(n_1, n_2)
f2 = fractions.Fraction(n_3, n_4)
print(f'Сумма {f1} и {f2} равна {f1 + f2}')
print(f'Произведение {f1} и {f2} равно {f1 * f2}')
