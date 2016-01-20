import math.factorial

for x in range(input()):
    rad = input()
    print round(sum([pow(-1, n) * pow(rad, 2 * n + 1) / math.factorial(2 * n + 1) for n in range(5)]), 3)
    print round(sum([pow(-1, n) * pow(rad, 2 * n) / math.factorial(2 * n) for n in range(5)]), 3)

