import re

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('but', 'ok'))

print('*'*50)
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
res = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(res)

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))

print('*'*50)

from calendar import month_abbr

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{}{}{}'.format(m.group(2), mon_name, m.group(3))

print(datepat.sub(change_date, text))
 
