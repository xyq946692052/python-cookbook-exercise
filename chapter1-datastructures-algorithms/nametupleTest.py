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


