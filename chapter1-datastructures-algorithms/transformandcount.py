nums = [1,2,3,4,5]
res = sum(x*x for x in nums)
print(res)

print('*'*50)

import os
files = os.listdir('../chapter1-datastructures-algorithms/')
print(files)
if any(name.endswith('.py') for name in files):
    print('There be pyhton!')
else:
    print('Sorry, no python.')

print('*'*50)
s = ('ACME', 50, 123.45)
print(', '.join(str(x) for x in s))

print('*'*50)
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'APPE', 'shares':250.9},
    {'name': 'AOL', 'shares':30.5},
    {'name': 'GPAS', 'shares': 50}
]
min_shares1 = min(s['shares'] for s in portfolio)
min_shares2 = min(portfolio, key=lambda s: s['shares']) 
print(min_shares1, min_shares2)
