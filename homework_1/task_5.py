# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

a_x: float = float(input('Enter X coordinate for A: '))
a_y: float = float(input('Enter Y coordinate for A: '))
b_x: float = float(input('Enter X coordinate for B: '))
b_y: float = float(input('Enter Y coordinate for B: '))

result = math.sqrt((b_x - a_x)**2 + (b_y - a_y)**2)
result = math.trunc(result * 100) / 100     #при использовании round(result, 2) - вместо 5,09 выводит 5.1 поэтому округление выполненно именно таким образом
print("The distance between two points is: " + str(result))
