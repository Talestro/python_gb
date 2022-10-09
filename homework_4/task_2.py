# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import math

number = int(input('Enter N number: '))
result_list = []
temp = 2

while temp * temp <= number:
    while number % temp == 0:
        result_list.append(math.trunc(temp))
        number = number / temp
    temp = temp + 1
if number > 1:
    result_list.append(math.trunc(number)) #trunc используется чтобы в списке не отображались числа с точкой

print(f'The prime factors of your number are: {result_list}')