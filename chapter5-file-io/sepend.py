print('ACEM', 50, 9.5)
print('ACEM', 50, 9.5, sep=', ')
print('ACEM', 50, 9.5, sep=', ', end='!!\n')

for i in range(5):
    print(i)

for i in range(5):
    print(i, end=' ')

tmp = ('ACEM', 5, 90)
print(*tmp, sep=':', end='\n')
