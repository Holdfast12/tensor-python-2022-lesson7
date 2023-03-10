#!/usr/bin/python3
# Написать функцию, принимающую сколько угодно параметров (в том числе и 0) и возвращающую их сумму.

def summ_of_args(*args):
    """Функция, принимающая сколько угодно числовых и текстовых параметров
    (в том числе и 0) и возвращающая их суммы.
    """
    t_numbers = 0
    t_strings = ''
    for i in args:
        if type(i) == int or type(i) == float:
            t_numbers += i
        elif type(i) == str:
            t_strings += i
    return t_numbers, t_strings

"""Получаем от пользователя параметры в переменную parameters
и пытаемся частично или полностью преобразовать элементы в числа
"""
parameters = input('Введите параметры через пробел, чтобы получить их сумму: ').split()
for i in range(len(parameters)):
    try:
        parameters[i] = float(parameters[i]) if '.' in parameters[i] else int(parameters[i])
    except ValueError:
        print(f'Параметр {parameters[i]} будет принят как текстовый')

summ_of_numbers, summ_of_strings = summ_of_args(*parameters)

print(f'=======================================\n\
        Для введенных параметров\n\
        \tсумма чисел будет равна: {summ_of_numbers}\n\
        \tсумма строк будет такой: {summ_of_strings}')
