s = '{name} has {n} messages.'.format(n=10, name='xyq')
print(s)

name = 'kevin'
n = 28
print(s.format(vars()))

class Info:
    def __init__(self, name, h):
        self.name = name
        self.n = n

a= Info('xyq', 28)
print(s.format_map(vars(a)))

class safesub(dict):
    def __nissing__(self, key):
        return '{' + key +'}'

del n
print(s.format_map(safesub(vars())))


import sys
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'kevin'
n=29
print(sub('hello {name}'))
print(sub('You have {n} messages.'))
print(sub('You favorite color is {color}.'))
