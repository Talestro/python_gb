# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

numbers_list = input('Enter list of numbers. Separate them with space: ').split()
index_start: int = 0
index_end: int = len(numbers_list) - 1
result_list = []

while index_start <= index_end:
    result_list.append(int(numbers_list[index_start]) * int(numbers_list[index_end]))
    index_start += 1
    index_end -= 1

print(f'Result is: {result_list}')
