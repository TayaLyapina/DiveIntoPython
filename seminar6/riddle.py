def guess_the_riddle(mystery, answers: list, attempts=3):
    print(mystery)

    for i in range(attempts):
        ans = input('Введите ответ: ')
        if ans in answers:
            return i + 1
        
    return 0

def play_guess_the_riddles(riddles):
    for riddle, answers in riddles.items():
        print('Загадка:')
        result = guess_the_riddle(riddle, answers)
        print(result)




