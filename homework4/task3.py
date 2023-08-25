# Задача 3.
# Возьмите задачу о банкомате из семинара. 
# Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

welcome = ('''
Команды для работы с банкоматом: 
Пополнение счета - 1
Снятие денег со счета - 2
Выход из программы - q 
''')

summ = 0
count_add = 0
count_out = 0
lst_operation = []


def add_money(amount, count, lst):
    amount = wealth_tax(amount)
    money_add = int(input("Введите сумму которую вы хотите положить на счет кратную 50: "))
    while money_add % 50 != 0:
        print("Сумма пополнения должна быть кратна 50")
        money_add = int(input("Введите сумму которую вы хотите положить на счет кратную 50: "))
    amount += money_add
    lst.append('add_money')
    count += 1
    print(count)
    amount = count_check(amount, count)
    return amount, count, lst
  
    
def withdraw_money(amount, count, lst):
    amount = wealth_tax(amount)
    mon = int(input("Введите сумму, которую хотите снять. Сумма должна быть кратна 50: "))
    while mon % 50 != 0:
        print("Сумма снятия должна быть кратна 50")
        mon = int(input("Введите сумму, которую хотите снять. Сумма должна быть кратна 50: "))
    proc = mon * 0.015
    if proc < 30:
        proc = 30
    elif proc > 600:
        proc = 600
    if mon + proc > amount:
        print("Недостаточно средств")
    else:
        amount -= mon + proc
        lst.append('money_out')
        count += 1
        print(count)
        amount = count_check(amount, count)
        return amount, count, lst
    
def count_check(amount, count):
    if count % 3 == 0:
        amount *=1.03
    return amount


def wealth_tax(amount):
    if amount > 5_000_000:
        print("С вас сняли налог на богатство", summ * 0.1)
        amount -= amount * 0.1
    return amount

action = None
while action != 'q':
    action = input(f'{welcome}').lower()
    if action == '1':
        summ, count_add, lst_operation = add_money(summ, count_add, lst_operation)
        print(summ)
        print(lst_operation)
    elif action == '2':
        summ, count_out, lst_operation = withdraw_money(summ, count_out, lst_operation)
        print(summ)
        print(lst_operation)
      
    