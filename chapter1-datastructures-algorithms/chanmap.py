from collections import ChainMap

a = {'x':10, 'y':20}
b = {'y':30, 'z':50}

c = ChainMap(a, b)

print(c['x'])
print(c['y'])
print(c['z'])


