# Задача.
# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных 
# файлов и директорий.

import csv
import json
import pickle
import os


def my_func(directory):
    all_directory = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            size_f = os.path.getsize(file_path)
            my_dict = {'name': file, 'parent_directory': root, 'object_type': 'file', 'size': size_f}
            all_directory.append(my_dict)
        for d in dirs:
            dir_path = os.path.join(root, d)
            size_d = 0
            for dirpath, dirs, filenames in os.walk(dir_path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    size_d += os.path.getsize(fp)
            my_dict = {'name': d, 'parent_directory': root, 'object_type': 'directory', 'size': size_d}
            all_directory.append(my_dict)
    print(all_directory)

    json_data = json.dumps(all_directory)
    with open('task.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)

    with open('task.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(all_directory[0].keys())
        for item in all_directory:
            writer.writerow(item.values())

    with open('task.pickle', 'wb') as pic_file:
        pickle.dump(all_directory, pic_file)


my_func('.\\seminar8')