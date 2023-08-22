# Задача 3.
# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. 
# *Верните все возможные варианты комплектации рюкзака.

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

# сбор вещей в порядке убывания веса

my_dict = dict(sorted(things.items(), key=lambda x: x[1], reverse=True))

# for k, v in my_dict.items():
#     print(k, ':', v)

backpack = {}
total_weight = 0
for key, value in my_dict.items():
    if total_weight + value <= max_weight:
        backpack[key] = value
        total_weight += value
        
print('Сбор вещей в порядке убывания веса: ')
for k, v in backpack.items():
    print(k, ':', v)

# сбор вещей в порядке возрастания веса

new_dict = dict(sorted(things.items(), key=lambda x: x[1]))
itog = {}
total_weight = 0
for key, value in new_dict.items():
    if total_weight + value <= max_weight:
        itog[key] = value
        total_weight += value

print('Сбор вещей в порядке возрастания веса: ')
for k, v in itog.items():
    print(k, ':', v)