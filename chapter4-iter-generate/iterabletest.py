from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [[3, 4, 5],6,], 7]
for x in flatten(items):
    print(x, end=", ")

strlst = ['apple', 'bannner', ['peach', 'origin']]
for x in flatten(strlst):
    print(x)
