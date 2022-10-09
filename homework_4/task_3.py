# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

default_sequence = [1, 2, 3, 4, 5, 6, 7, 4, 3, 21, 1, 2, 6, 9, 0, 43]
unique_numbers = list(set(default_sequence))
print(f'Default sequence is: {default_sequence}\n Unique numbers of this sequence is: {unique_numbers}')

unique_numbers = []
temp = 0

for i in default_sequence:
    if i not in unique_numbers:
        unique_numbers.append(i)

print(f'Result without set func: {unique_numbers}')
