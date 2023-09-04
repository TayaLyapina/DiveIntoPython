_dct = {}


def func(que, count):
    print(que)
    a = 'в правде'

    i = 0
    while count > i:
        ans = input('Напишите ответ >')
        if ans == a:
            _dct[i + 1] = 'Вы угадали'
            return
        else:
            _dct[i + 1] = 'не угадал'
            i += 1

func('В чем сила: ', 3)
print(_dct)