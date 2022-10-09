# Вычислить число ПИ c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

calculation_accuracy = int(input('Enter accuaracy for calculation Pi (from 1 to 10) numbers after the decimal point: '))

result_round = round(2 * math.acos(0.0), calculation_accuracy)
result_without_round = (math.trunc((2 * math.acos(0.0)) * 10 ** calculation_accuracy)) / 10 ** calculation_accuracy
print(f'Using arc cosine with round: {result_round}, and without round: {result_without_round}')

result_round = round(math.pi, calculation_accuracy)
result_without_round = (math.trunc(math.pi * 10 ** calculation_accuracy)) / 10 ** calculation_accuracy
print(f'Using math lib with round: {result_round}, and without round: {result_without_round}')

