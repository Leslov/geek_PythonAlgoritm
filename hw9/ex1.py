# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1()
# или любой другой из модуля hashlib задача считается не решённой.

def get_subrows_count(string: str):
    def foreach_all_subrows(source):
        source_len = len(source)
        for l in range(1, source_len): # Длина подстроки
            for s in range(0, source_len - l + 1): # индекс подстроки
                yield source[s:s+l]
    rows_dict = {}
    rows = foreach_all_subrows(string)
    for row in rows:
        key = hash(row)
        if not rows_dict.__contains__(key):
            rows_dict[key] = 1
        else:
            rows_dict[key] += 1
    return len(rows_dict.keys())


mystr = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et ' \
        'dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ' \
        'ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu ' \
        'fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt ' \
        'mollit anim id est laborum'
print(get_subrows_count(mystr))