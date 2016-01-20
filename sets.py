__author__ = 'shelan'
input()
a = raw_input().split()
input()
b = raw_input().split()

a_ints = map(int, a)
b_ints = map(int, b)

a_set = set(a_ints)
b_set = set(b_ints)

a_union_b = a_set.union(b_set)
a_intersection_b = a_set.intersection(b_set)
print sorted(set(a_union_b - a_intersection_b))

