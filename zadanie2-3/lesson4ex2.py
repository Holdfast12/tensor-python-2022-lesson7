#!/usr/bin/python3
# Создать словарь цветов, в котором ключ - название или кодировка цвета; значение - кортеж из rgb этого цвета.

colors = {
        'red': (255, 0, 0),
        'green': (0, 128, 0),
        'black': (0, 0, 0),
        }

print(f'Словарь цветов: {colors}')

#записать свой цвет
print('Добавление цвета')
l = input('Введите название своего цвета: ')
colors[l] = tuple(map(int, input('Введите 3 значения rgb нового цвета: ').split()))
print(f'Словарь цветов: {colors}')
