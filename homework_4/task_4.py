# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

degree_k = int(input('Enter highest degree for polynomial: '))
min_lim = 0
max_lim = 100
list_of_coefficients = []

for i in range(degree_k + 1):
    if i == 0:
        list_of_coefficients.append(random.randint(min_lim + 1, max_lim))   #чтобы не занулялся первый коэффициент
    else:
        list_of_coefficients.append(random.randint(min_lim, max_lim))

with open('polynomials', 'a') as f:

    for i in range(len(list_of_coefficients)):
        if i == 0:
            f.write(f'{list_of_coefficients[i]}*x^{len(list_of_coefficients) - 1}')
        elif list_of_coefficients[i] != 0 and (i != len(list_of_coefficients) - 1):
            f.write(f' + {list_of_coefficients[i]}*x^{len(list_of_coefficients) - i - 1}')
        elif (i == len(list_of_coefficients) - 1) and list_of_coefficients[i] != 0:
            f.write(f' + {list_of_coefficients[i]}')
        else:
            continue
    f.write(' = 0\n')
