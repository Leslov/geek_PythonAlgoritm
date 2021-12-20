# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться,
# больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.
import random
import helpers

num = random.randint(0, 100)
guess_count_remaining = 3
print(num)
print('Компьютер загадал число. На его угадывание вам дается 10 попыток')
while guess_count_remaining > 0:
    guessed = helpers.input_by_type('', int)
    if guessed == num:
        print('Угадал!')
        break
    elif num > guessed:
        print(f'Загаданное число больше чем {guessed}')
    else:
        print(f'Загаданное число меньше чем {guessed}')
else:
    print(f'Попытки закончились. Загаданное число = {num}')