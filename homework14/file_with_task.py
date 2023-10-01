# Задание №2
# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений

def get_dict(my_dict, key, default_value='None'):
    try:
        return my_dict[key]
    except KeyError:
        return default_value


my_d = {1: 'one', 2: 'two', 3: 'three'}
if __name__ == '__main__':
    print(get_dict(my_d, 1, '1'))
    print(get_dict(my_d, 'a'))