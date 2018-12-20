import math

a = float('inf')
b = float('-inf')
c = float('nan')
print(a, b, c, math.isinf(a), math.isnan(c))

print(a+45)
print(a/a)
print(a+b)
print(a/b)
print(10/a)

c = float('nan')
d = float('nan')
print(c==d)
print(c is d)
