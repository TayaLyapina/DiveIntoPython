import date_chek

result = date_chek.check_date(input('Введите дату в формате DD.MM.YYYY: '))

if result == True:
    print("Такая дата существует")
else:
    print("Такой даты нет")