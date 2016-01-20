__author__ = 'shelan'

tests = input()

for tests in range(tests):
    limit = input()
    five_N = limit // 5 if limit % 5 > 0 else (limit // 5) - 1
    three_N = limit // 3 if limit % 3 > 0 else (limit // 3) - 1
    fifteen_N = limit // 15 if limit % 15 > 0 else (limit // 15) - 1

    print ((5 * five_N * (five_N + 1) * 1/2) + (3 * three_N * (three_N + 1) * 1/2)  - (15 * fifteen_N * (fifteen_N + 1) * 1/2))



