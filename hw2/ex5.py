#5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

min = 32
max = 127
counter = 0

for i in range(min, max):
    counter += 1
    char = {i: chr(i)}
    if counter == 10:
        counter = 0
        print(char)
    else:
        print(char, end='\t')