from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('xyq@sina.com', '2018-12-11')
print(sub, sub.addr, sub.joined)

addr, joined = sub
print(addr, joined)


Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    totle = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

s = Stock('ACME', 100, 12.0)
print(s, s.name, s.shares, s.price)

# if change the value of nametuple, you need use _replace
s = s._replace(shares=200)
print(s)


Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)

# Function to convert a dictinary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares':100, 'price':123.45}
print(dict_to_stock(a))
b = {'name':'ACME', 'shares':100, 'price':123.45, 'date':'12/12/2018'}
print(dict_to_stock(b))
