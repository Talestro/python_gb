# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_number: int = int(input('Enter day number: '))
if day_number > 8 ^ day_number < 1:
    print("Day number does not exist. Try again")
elif day_number == 6 ^ day_number == 7:
    print('да')
else:
    print('нет')


