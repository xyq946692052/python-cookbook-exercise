
mylst = [1,2,4,7,9,-2,4,6,-12,5,-8]

zlst = [x for x in mylst if x>0]
flst = [x for x in mylst if x<0]

print(zlst,'\n', flst) 


# if generate the list is larget, change generate replace list to reduce memory footprint
pos = (n for n in range(1000000))
print(pos)
#for i in pos:
#    print(i, end='')


# if fiter the complex data, need to do like this
values = ['1', '3','a', '4', 'None', 'b', '100']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

res = list(filter(is_int, values))
print(res)


# use itertools.compress to fiter data
addresses = [
    '5412 N CLARK',
    '5312 N CLARK',
    '2342 E ABS',
    '4567 W EROP',
    '2366 E AMER',
    '6321 S AUTR',
    '5825 E RUSS',  
    '4560 N FREW'
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress
more5 = [n>5 for n in counts]
print(more5)
res = list(compress(addresses, more5))
print(res)

