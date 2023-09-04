# Задача 1.
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from sys import argv
import date_check 

date = argv[1]
print(date_check.check_date(date))
