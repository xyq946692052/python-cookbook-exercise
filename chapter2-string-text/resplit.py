import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
res1 = re.split(r'[;,\s]\s*', line)
print(res1)

res2 = re.split(r'(;|,|\s)\s*', line)
print(res2)

values = res1[::2]
print(values)
delimiters = res1[1::2] + ['']
print(delimiters)

# Reform the line using the same delimiters
c = ''.join(v+d for v, d in zip(values, delimiters))
print(c)


