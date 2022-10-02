# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n_number: int = int(input("Enter N: "))
sequence_dict = {}
index: int = 1

for i in range(n_number):
    sequence_dict[index] = 3*index+1
    index += 1

print(f'For n = {n_number}: {sequence_dict}')
