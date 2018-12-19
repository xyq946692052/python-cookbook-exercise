parts = ['Is', 'Chicago', 'Not', 'Chicago']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))

a = 'Is Chicago'
b = 'Not Chicago'
print('{} {}'.format(a, b))
print(a + ' ' + b)

data = ['ACME', 50, 10.25,]
res = ','.join(str(x) for x in data)
print(res)

