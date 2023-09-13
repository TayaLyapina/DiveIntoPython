# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import random
from typing import Callable
import json
import csv
from functools import wraps


def decorator_square_root(func: Callable):
    @wraps(func)
    def wrapper(filename):
        result = []
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(float, row)
                res = func(a, b, c)
                result.append(res)
            return result
    return wrapper


def log_decorator(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        data = {
            'func': func.__name__,
            'parameters': {'args': args, 'kwargs': kwargs},
            'result': result
        }
        with open('log.json', 'w+', encoding='utf-8') as f:
            json.dump(data, f)
        return result
    return wrapper


@decorator_square_root
@log_decorator
def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return root1, root2


def gen_csv(filename):
    rows = random.randint(10, 101)
    with open(filename, 'a', newline='', encoding='utf-8') as file_csv:
        writer = csv.writer(file_csv)
        for _ in range(rows): 
            writer.writerow([random.randint(1, 50) for _ in range(3)])


gen_csv('gen_ns.csv')
find_roots('gen_ns.csv')