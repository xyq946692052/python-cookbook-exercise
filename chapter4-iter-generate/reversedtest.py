lst = [1, 2, 3, 4, 5, 6, 7, 8]
for x in reversed(lst):
    print(x, end=', ')

print(lst[::-1])

print("*"*50)

import os

flst = os.listdir(os.getcwd())
f = open(flst[0])
for line in reversed(list(f)):
    print(line, end='')
