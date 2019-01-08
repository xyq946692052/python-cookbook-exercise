add = lambda x,y: x+y
print(add(1, 2))
print(add(2,3))

names = ['Peter Xie', 'Ken Wu', 'Anne Li', 'Sue Si']
res = sorted(names, key=lambda name: name.split()[-1].lower())
print(res)
