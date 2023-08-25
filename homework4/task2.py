# Задача 2.
# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.


def my_func(**kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        if not isinstance(key, (int, float, bool, tuple)):
            key = str(key)
        my_dict[value] = key
    return my_dict

arguments = my_func(s='text', name='Taya', profession='student')
print(arguments)