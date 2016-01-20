__author__ = 'shelan'

x_range = input()
y_range = input()
z_range = input()
N = input()
print [[x, y, z] for x in range(x_range + 1) for y in range(y_range + 1) for z in range(z_range + 1) if x + y + z != N]