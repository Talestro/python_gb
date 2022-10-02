# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n_number: int = int(input('Enter N: '))
results = []
index: int = 0


def multi(number):
    mult, count = 1, 0
    while number > 0:
        mult *= number
        number -= 1
    return mult


for i in range(n_number):
    results.append(multi(index+1))
    index += 1

print(f'For n = {n_number} list is: {results}')
