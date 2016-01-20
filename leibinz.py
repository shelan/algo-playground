from math import exp

__author__ = 'shelan'

for x in range(input()):
    print sum([pow(-1,y) / float(2 * y + 1) for y in range(input())])


# print reduce(sum,gen)

