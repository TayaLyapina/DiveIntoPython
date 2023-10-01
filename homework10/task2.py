# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали. 
# Превратите функции в методы класса, а параметры в свойства. 
# Задания должны решаться через вызов методов экземпляра

# Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых 
# pickle файлов.

import json
import pickle
import os


class JsonToPickle:

    def __init__(self, directory):
        self.directory = directory


    def convert_json_to_pickle(self):
        for filename in os.listdir(self.directory):
            if filename.endswith('json'):
                with open(filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            
                pickle_data_name = filename.split('.')[0] + '.pickle'
                with open(pickle_data_name, 'wb') as fp:
                    pickle.dump(data, fp)


converter = JsonToPickle('./seminar8/test')
converter.convert_json_to_pickle()