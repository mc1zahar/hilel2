# part_1

a = 5
b = 6
print('before : a =', a, 'b =', b)
c = b
b = a
a = c
print('after : a =', a, 'b =', b)

# part_2

print('before : a =', a, 'b =', b)
a, b = b, a
print('after : a =', a, 'b =', b)

# part_3
a = 5
b = 8

a = a + b   # a = 13, b = 8
b = a - b   # a = 13, b = 5
a = a - b   # a = 8, b = 5

print('a =', a, 'b =', b)
