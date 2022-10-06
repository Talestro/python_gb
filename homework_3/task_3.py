# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

list_size = int(input('Enter list length: '))
default_list = []

for i in range(list_size):
    default_list.append(round(random.uniform(0, 20), 2))  #интервал выбран произвольно чтобы не запрашивать пользователя

print(f'Generated list is: {default_list}')

fractional_parts_list = []
index: int = 0

for i in range(list_size):
    fractional_parts_list.append(default_list[index] * 100 % 100)
    index += 1

result = (max(fractional_parts_list) - min(fractional_parts_list)) / 100

print(f'Result is: {result}')
