my_list = ['a', 'b', 'c']

for idx, val in enumerate(my_list):
    print(idx, val)

print('*'*50)

for idx, val in enumerate(my_list, 1):
    print(idx, val)

print('*'*50)

from collections import defaultdict
import heapq
import os

word_summary = defaultdict(list)

fname = os.listdir(os.getcwd())
fsize = [os.path.getsize(x) for x in fname]
fdt = dict(zip(fname, fsize))
f_max = sorted(fdt.items(), key=lambda d:d[1])[-1][0]

with open(f_max, 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(lines)

for idx, line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

print(word_summary)


