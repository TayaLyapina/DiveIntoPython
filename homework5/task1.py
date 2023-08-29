# Задача 1.
# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

import os

def file_info(x: str):
    file_dir = os.path.dirname(x)
    file_name = os.path.basename(x)
    file_ext = os.path.splitext(x)[1]
    return file_dir, file_name, file_ext


absolute_path = r'C:\Users\user\Downloads\photo.jpg' 
my_tuple = file_info(absolute_path)
print(my_tuple)