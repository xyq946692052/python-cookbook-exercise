import re

s = ' hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

t = '----------hello=========='
print(t.lstrip('-'))
print(t.rstrip('='))
print(t.strip('-='))

s = 'hello       world'
print(s.replace(' ',''))

print(re.sub('\s+', ' ', s))

with open('searchandreplace.py') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)
