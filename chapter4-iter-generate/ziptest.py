xpts = [1, 2, 3, 4, 5, 6]
ypts = ['a', 'b', 'c', 'd', 'e', 'f']

for x, y in zip(xpts, ypts):
    print(x, y)


print('*'*50)

zpts = ['python', 'golang', 'django', 'wexin']

for x, z in zip(xpts, zpts):
    print(x, z)

print('*'*50)

from itertools import zip_longest

for i in zip_longest(xpts, zpts):
    print(i)

print('*'*50)

for i in zip_longest(xpts, zpts, fillvalue=0):
    print(i)
