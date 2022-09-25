# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_number: int = int(input('enter quarter number: '))

if (quarter_number == 1):
    print(f"For {quarter_number} quarter: X from 0 to inf+, and Y from 0 to inf+")
elif (quarter_number == 2):
    print(f"For {quarter_number} quarter: X from inf- to 0, and Y from 0 to inf+")
elif (quarter_number == 3):
    print(f"For {quarter_number} quarter: X from inf- to 0, and Y from inf- to 0")
elif (quarter_number == 4):
    print(f"For {quarter_number} quarter: X from 0 to inf+, and Y from inf- to 0")
else:
    print(f"{quarter_number} quarter doesn't exist")
