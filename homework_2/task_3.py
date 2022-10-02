# Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:
# - Для n = 5: сумма = 11,55

n_number: int = int(input("Enter N: "))
sequence_list = []
sum: int = 0
count: int = 1

for i in range(n_number):
    sequence_list.append((1+(1/count))**count)
    count += 1
    sum += sequence_list[i]

print(f'For n = {n_number}: sum is = {round(sum,2)}')
