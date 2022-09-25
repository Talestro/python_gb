# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x_coordinate: int = int(input('Enter X coordinate: '))
y_coordinate: int = int(input('Enter Y coordinate: '))

if (x_coordinate == 0 or y_coordinate == 0):
    if (x_coordinate == 0):
        print('The point lies on the axis X')
    else:
        print('The point lies on the axis Y')
elif (x_coordinate > 0 and y_coordinate > 0):
    print('The point in 1 quarter')
elif (x_coordinate < 0 and y_coordinate < 0):
    print('The point in 3 quarter')
elif (x_coordinate > 0 and y_coordinate < 0):
    print('The point in 4 quarter')
else:
    print('The point in 2 quarter')
