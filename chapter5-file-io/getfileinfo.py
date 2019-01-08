import os
import glob

path = '/home/xyq/python-cookbook-exercise/chapter5-file-io'
pyfiles = glob.glob('*.py')

print(pyfiles)

name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name)) 
                for name in pyfiles]

for name, size, mtime in name_sz_date:
    print(name, size, mtime, sep=', ')

print('*'*50)

file_metadata = [(x, os.stat(name)) for x in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
