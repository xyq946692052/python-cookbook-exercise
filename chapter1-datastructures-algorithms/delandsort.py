# remove the repeat item and order the same


items = [1,3,6,2,5,3,9,0,1,5,3]
print('items: ', items)


# way 1
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

print(list(dedupe(items)))


# way 2
lst = sorted(set(items), key=items.index)
print(lst) 


# way 3
n = []
lst = [n.append(item) for item in items if not item in n]
print(n)


# remove the same item in dict
def dedquedict(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

dt = [{'x':1, 'y':2},{'x':1, 'y':3},{'x':1,'y':2}, {'x':2, 'y':4}]
lst = list(dedquedict(dt, key=lambda d: (d['x'], d['y'])))
print(lst)

