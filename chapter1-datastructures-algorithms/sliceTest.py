# use slice replace index of hard slice

items = [1,2,3,4,5,6,7,8,9,0]
print('items: ',items)

a = slice(1,4,2)
print(items[a])  # this way is more clearly  than items[1:3]

# replace
items[a] = ['a','b']
print(items)

del items[a]
print(items)

print(a.start, a.stop, a.step)
