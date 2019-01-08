import os

path = '/home/xyq/python-cookbook-exercise/chapter5-file-io'
name = os.listdir(path)
print(name)

#get all regular files
names = [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, 'strandbyteio.py'))]

print(names)

#get all dirs
dirnames = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, 'strandbyteio.py'))]
print(dirnames)

pyfiles = [x for x in os.listdir(path) if x.endswith('.py')]
print(pyfiles)


startwiths = [x for x in os.listdir(path) if x.startswith('f')]
print(startwiths)

import glob
pyfs = glob.glob(path+'/*.py')
print(pyfs)

from fnmatch import fnmatch
pyfns = [x for x in os.listdir(path) if fnmatch(x, '*.py')]
print(pyfns)
