# Задание
# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv


class NameValidator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if value.istitle() == False or value.isalpha() == False:
            raise ValueError(f'{value} должно состоять только из букв и начинаться с заглавной буквы')
        instance.__dict__[self.name] = value


class Student:
    first_name = NameValidator()
    middle_name = NameValidator()
    last_name = NameValidator()

    def __init__(self, first_name, middle_name, last_name, file_csv):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        
        with open(file_csv, 'r', encoding='utf-8') as csv_f:
            reader = csv.reader(csv_f)
            self.subjects = {row[0]: {"grades": [], "test_scores": []} for row in reader}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден.")
        if grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть от 2 до 5.")
        self.subjects[subject]["grades"].append(grade)
        
    def add_test_score(self, subject, test_scores):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден.")
        if test_scores < 0 or test_scores > 100:
            raise ValueError("Результат теста должен быть от 0 до 100.")
        self.subjects[subject]["test_scores"].append(test_scores)

    def average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден.")
        scores = self.subjects[subject]["test_scores"]
        return sum(scores) / len(scores) if scores else 0    
    
    def average_grade(self):
        total_grades = [grade for subj in self.subjects.values() for grade in subj["grades"]]
        return sum(total_grades) / len(total_grades) if total_grades else 0
    

student = Student('Ивенов', 'Иван', 'Иванович', 'sub.csv')
student.add_grade("Математика", 4)
student.add_grade("Математика", 5)
student.add_test_score("Математика", 80)
student.add_test_score("Математика", 90)
student.add_grade("Физика", 3)
student.add_grade("Физика", 4)
student.add_test_score("Физика", 90)

average_grade = student.average_grade()
average_test_score = student.average_test_score("Математика")

print("Средний балл по оценкам:", average_grade)
print("Средний балл по тестам по Математике:", average_test_score)
