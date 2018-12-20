a = 4.2
b = 2.1

print(a+b)

print((a+b)==6.3)

print('*'*50)

from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print(a+b)
print((a+b) == Decimal('6.3'))

print('*'*50)

from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a/b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a/b)
