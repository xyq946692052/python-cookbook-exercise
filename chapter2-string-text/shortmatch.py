import re

str_pat = re.compile(r'"(.*)"')
t1 = 'Computer says "no."'
print(str_pat.findall(t1))

t2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(t2))


print('*'*50)
str_pat = re.compile(r'"(.*?)"')
print(str_pat.findall(t2))
