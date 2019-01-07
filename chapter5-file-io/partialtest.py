from functools import partial
import gzip

RECORD_SIZE = 5

with open('binaryfile.py', 'rt') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)
