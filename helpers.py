def is_int(value):
    try:
        int(value)
        return True
    except:
        return False


def input_by_type(input_text, type, validate=None):
    if not callable(type):
        raise ValueError('Атрибут type должен быть функцией')
    while True:
        try:
            value = type(input(input_text))
            if callable(validate) and not validate(value):
                continue
            return value
        except Exception as e:
            print(e)
            print(f'Введенное значение не является {type}. Повторите ввод')


def get_positive_number(message, type):
    while True:
        result = input_by_type(message, type)
        if result > 0:
            return result
        else:
            print('Число должно быть больше нуля')


def try_cast(value, type, default_value=None):
    if not callable(type):
        raise ValueError('Атрибут type должен быть функцией')
    try:
        return type(value)
    except:
        return default_value

def run_exercise_selector(exercises):
    end = False
    last_index = len(exercises)
    while not end:
        msg = f'Введите номер упражнения для проверки. От 1 до {last_index}. Или любую клавишу для завершения: '
        exc = input(msg)
        exc_num = try_cast(exc, int, -1)

        if exc_num <= 0 or exc_num > last_index:
            break
        print('\n****************\n')
        print(f'Упражнение №{exc_num}')
        exercises[exc_num - 1]()
        print('\n****************\n')


def average(my_list):
    return sum(my_list)/len(my_list)


def get_values_from_user(text, count, type: callable, validator=None):
    arr = []
    for i in range(count):
        arr.append(input_by_type(f'{text} №{i+1} ', type, validator))
    return arr
