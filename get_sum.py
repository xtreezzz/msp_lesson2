def get_summ(_num_one, _num_two):
    try:
        return int(_num_one) + int(_num_two)
    except ValueError as err:
        print(f'Не могу привести входные аргументы [{_num_one} или {_num_two}] к int \n'
              f'Ошибка: {err}')


while True:
    try:
        one, two = input('Введите первое и второе число через пробел: ').split(' ')
        if len(one) + len(two) < 2:
            raise ValueError
        elif len(one) == 0 or len(two) == 0:
            raise ValueError
        break
    except ValueError as err:
        print('Ошибка ввода повторите')