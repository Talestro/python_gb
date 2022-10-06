# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

user_number: int = int(input('Enter number for transition: '))
remain_of_number: str = ''

while user_number > 0:
    remain_of_number = str(user_number % 2) + remain_of_number
    user_number = user_number // 2

print(f'Result of translation is: {remain_of_number}')
