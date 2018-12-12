from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))

print(fnmatch('foo.txt','*.TXT'))  #if window, this is True, if linux is  False
print(fnmatchcase('foo.txt', '*TXT'))  # stick to match capital and small letter

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

print([x for x in addresses if fnmatchcase(x, '* ST')])
print([x for x in addresses if fnmatchcase(x, '54[0-9][0-9] *CLARK*')]) 
