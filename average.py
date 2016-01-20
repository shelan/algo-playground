__author__ = 'shelan'
import math

# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika


num_of_students = input()
students = {}

for i in range(num_of_students):
    row = raw_input().split(' ')
    name = row[0]
    marks = row[1:]

    students[name] = marks

name = raw_input()
avg = sum(list([float(i) for i in students[name]]))/len(students[name])
print format(avg,'.2f')