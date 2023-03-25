# Проект 1. Бейглз

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''Бейглз, дедуктивная логическая игра.

Я задумываю число из {} неповторяющихся цифр.
Попробуйте угадать его. Вот подсказки:

Когда я говорю:     Это значит:
    Пико            Одна цифра правильная, но находится на неправильной позиции
    Ферми           Одна цифра правильная и находится на правильной позиции
    Бублики         Правильных цифр нет

Например, если секретное число 248 и ваша догадка 843,
подсказкой будет "Пико Ферми".'''.format(NUM_DIGITS)) 
    while True:
        secretNum = getSecretNum()
        print('Я загадал число.')
        print('У вас есть {} попыток, чтобы угадать его.'.format(MAX_GUESSES))
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Попытка №{}: '.format(numGuesses))
                guess = input('> ')
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            if guess == secretNum:
                break
            if numGuesses >= MAX_GUESSES:
                print('У вас закончились попытки.')
                print('Правильным числом было {}.'.format(secretNum))
        print('Хотите сыграть снова? (Да или Нет)')
        if not input('> ').lower().startswith('Д'):
            break
    print ('Спасибо за игру!')

def getSecretNum():
    numbers = list('0123456789')
    secretNum = ''
    random.shuffle(numbers)
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'Правильно!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Ферми')
        elif guess[i] in secretNum:
            clues.append('Пико')
    if len(clues) == 0:
        return 'Бублики!'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()
