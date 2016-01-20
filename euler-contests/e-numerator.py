__author__ = 'shelan'

last = input()


def calcuate_digit_sum(number):
    digits = map(int, str(number))
    return sum(digits)

first, second = 1, 2

for i in range(2, last + 1):
    tmp_first = second
    second = first + second * (1 if i % 3 else 2 * i // 3)
    first = tmp_first

print calcuate_digit_sum(second)

