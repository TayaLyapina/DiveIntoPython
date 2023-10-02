# Задание
# Возьмите любые 1-3 задачи из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации. 
# Также реализуйте возможность запуска из командной строки с передачей параметров.

import argparse
import logging
import csv


logging.basicConfig(filename='student.log', 
                    encoding='utf-8',
                    format='{levelname:<7} - {asctime} : {msg}',
                    style='{',
                    level=logging.INFO,)
logger = logging.getLogger(__name__)


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
    

def main():
    parser = argparse.ArgumentParser(description='Process student information.')
    parser.add_argument('first_name', help='Student first name')
    parser.add_argument('middle_name', help='Student middle name')
    parser.add_argument('last_name', help='Student last name')
    parser.add_argument('file_csv', help='CSV file')
    args = parser.parse_args()

    try:
        student = Student(args.first_name, args.middle_name, args.last_name, args.file_csv)
        # student.add_grade("История", 4)
        student.add_grade("Математика", 6)
       
    except InvalidNameError:
        logging.error('Invalid student name format.')
    except InvalidSubjectError as e:
        logging.error(f'Invalid subject: {e.subject}')
    except InvalidGradeError as e:
        logging.error(f'Invalid grade: {e.grade}')
    except InvalidTestScoreError as e:
        logging.error(f'Invalid score: {e.test_scores}')

    logger.info(f'Успешно')

if __name__ == '__main__':
    main()