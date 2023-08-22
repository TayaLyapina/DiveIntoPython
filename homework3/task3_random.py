# Задача 3.
# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. 
# *Верните все возможные варианты комплектации рюкзака.

import random

things = {"палатка": 5240, 
          "зонт": 1000, 
          "рубашка": 500, 
          "брюки": 1000, 
          "ботинки": 1200, 
          "спички": 100, 
          "соль": 100, 
          "крупа": 1000,
          "карандаш": 20,
          "бумага": 200,
          "расческа": 50,
          "котелок": 850,
          "ведро": 1000,
          "удочка": 800,
          "хлеб": 1000,
          "зеркальце": 100,
          "молоток": 700,
          "пила": 500,
          "консервы": 500}

max_weight = 10000 # грузоподъемность рюкзака 10 кг

backpack = {}
total_weight = 0.0
for key, value in things.items():
    random_weight = random.choice(list(things.values()))
    if total_weight + random_weight <= max_weight:
        if random_weight not in backpack.values():
            backpack[key] = random_weight
            total_weight += random_weight

print("Вещи, которые влезут в рюкзак:")
for item, weight in backpack.items():
    print(f"{item}: {weight} кг")