import heapq

a = [1, 4, 7, 10]
b = [2, 5, 6, 9, 0, 3]

for c in heapq.merge(a, b):
    print(c)

