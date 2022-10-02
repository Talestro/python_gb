# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n_number: int = int(input("Enter N: "))
data_list = []
result: int = 1

f = open('file.txt', 'r')
positions = f.readlines()
f.close()


def add_values_to_list(n, list_for_fill=[]):
    start, stop = -n, n+1
    while start < stop:
        list_for_fill.append(start)
        start += 1


add_values_to_list(n_number, data_list)
index: int = 0

for i in range(len(positions)):
    if int(positions[index]) < len(data_list):
        result *= data_list[int(positions[index])]
    index += 1

print(f'Data list is: {data_list} \n positions for multiplication is: {positions} \n result is: {result}')
