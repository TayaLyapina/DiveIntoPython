# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

class Factory:

    def create_animal(self, animal_type, name, age, breed, color):
        if animal_type == 'Bird':
            return Bird(name, age, breed, color)
        if animal_type == 'Cat':
            return Cat(name, age, breed, color)
        if animal_type == 'Fish':
            return Fish(name, age, breed, color)


class Bird:
    def __init__(self, name, age, breed, color):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color


    def info_birds(self):
        return f'Птичка {self.name} относится к отряду {self.breed} и имеет расцветку {self.color}.'



class Cat:
    def __init__(self, name, age, breed, color):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color


    def info_cat(self):
        return f'Кошка {self.name} породы {self.breed} и  имеет окрас {self.color}.'


class Fish:
    def __init__(self, name, age, breed, color):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color


    def info_fish(self):
        return f'Рыбка {self.name} относится к породе {self.breed} и {self.color} окраса.'


factory = Factory()

b = factory.create_animal('Bird', 'Феня', 8, 'попугай', 'зелёных, красных, голубых и жёлтых тонов')
print(b.info_birds())

c = factory.create_animal('Cat', 'Плюшка', 6, 'британская, вислоухая', 'серо-голубой, сплошной')
print(c.info_cat())

f = factory.create_animal('Fish', 'Немо', 1, 'скалярия', 'зеленовато-серого с серебристым отливом')
print(f.info_fish())