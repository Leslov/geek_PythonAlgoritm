from collections import namedtuple

import helpers

print('1. Пользователь вводит данные о количестве предприятий,\n'
      'их наименования и прибыль за четыре квартала для каждого предприятия.\n'
      'Программа должна определить среднюю прибыль (за год для всех предприятий)\n'
      'и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.')


def print_facilities(fac_arr, text):
    if any(fac_arr):
        print(text)
        for fac in fac_arr:
            print(f'"{fac.name}": {fac.income}')


# Подготовка данных
facilities_count = helpers.input_by_type('Введите количество предприятий: ', int)
facilities = [None] * facilities_count
Facility = namedtuple('facility', 'name, income')
for i in range(facilities_count):
    print(f'\nВведите данные предприятия №{i + 1}')
    name = input('Введите название: ')
    income = helpers.input_by_type('Введите прибыль: ', float, lambda x: x > 0)
    facilities[i] = Facility(name, income)

# Подсчет результатов
print('*' * 50)
average_income = sum([x.income for x in facilities]) / facilities_count
less_than_average = [x for x in facilities if x.income < average_income]
greater_than_average = [x for x in facilities if x.income > average_income]

# Печать результатов
print(f'Средняя прибыль: {average_income}')
print_facilities(less_than_average, f'\nПредприятия с прибылью ниже средней:')
print_facilities(greater_than_average, f'\nПредприятия с прибылью выше средней:')
