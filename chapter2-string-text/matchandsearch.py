import re

# find, startswith, endswith

text = 'yeah, but no, but yeah, but no, but yeah'
print(text == 'yeah')
print(text.startswith('yeah'))
print(text.endswith('no'))
print(text.find('but'))

print('*'*50)
t1 = '12/12/2018'
t2 = 'Nov 12, 2018'
# Simple matching: \d+ means match one or more digits

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(t1):
    print('yes')
else:
    print('no')

if datepat.match(t2):
    print('yes')
else:
    print('no')

t3 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(t3))


print('*'*50)
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('12/12/2018')
print(m)
print(m.group(0), m.group(1), m.group(2), m.group())
month, day, year = m.groups()
print(month, day, year)

print(datepat.findall(t3))
for month, day, year in datepat.findall(t3):
    print('{}-{}-{}'.format(year, month, day))

for m in datepat.finditer(t3):
    print(m.groups())


