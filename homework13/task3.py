import csv

class InvalidNameError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name} должно состоять только из букв и начинаться с заглавной буквы'


class InvalidSubjectError(Exception):
    def __init__(self, subject):
        self.subject = subject

    def __str__(self):
        return f'Предмет {self.subject} не найден.'
    

class InvalidGradeError(Exception):
    def __init__(self, grade):
        self.grade = grade

    def __str__(self):
        return f'Оценка = {self.grade}, а должна быть от 2 до 5.'
    

class InvalidTestScoreError(Exception):
    def __init__(self, test_scores):
        self.test_scores = test_scores

    def __str__(self):
        return f'Результат теста = {self.test_scores}, а  должен быть от 0 до 100.'


class Student:

    def __init__(self, first_name, middle_name, last_name, file_csv):
        if first_name.istitle() == False or first_name.isalpha() == False:
            raise InvalidNameError(first_name)
        if middle_name.istitle() == False or middle_name.isalpha() == False:
            raise InvalidNameError(middle_name)
        if last_name.istitle() == False or last_name.isalpha() == False:
            raise InvalidNameError(last_name)
        
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        
        with open(file_csv, 'r', encoding='utf-8') as csv_f:
            reader = csv.reader(csv_f)
            self.subjects = {row[0]: {"grades": [], "test_scores": []} for row in reader}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise InvalidSubjectError(subject)
        if grade < 2 or grade > 5:
            raise InvalidGradeError(grade)
        
        self.subjects[subject]["grades"].append(grade)
        
    def add_test_score(self, subject, test_scores):
        if subject not in self.subjects:
            raise InvalidSubjectError(subject)
        if test_scores < 0 or test_scores > 100:
            raise InvalidTestScoreError(test_scores)
        
        self.subjects[subject]["test_scores"].append(test_scores)

    def average_test_score(self, subject):
        if subject not in self.subjects:
            raise InvalidSubjectError(subject)
        
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
