# Задача 5.
# Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии. 


def get_premium_amount(a: list[str], b: list[int], c: list[str], data=None):
    if data is None:
        data = {}
    c = [float(i[:-1]) for i in c]
    for i in range(len(a)):
        data[a[i]] = b[i] * c[i] / 100
    return data

        
names = ['Alex', 'Tasha', 'Misha', 'Oleg']
rate = [40000, 20000, 70000, 11000]
premium = ['10.25%', '45.03%', '50.5%', '10.99%']

print(get_premium_amount(names, rate, premium))
