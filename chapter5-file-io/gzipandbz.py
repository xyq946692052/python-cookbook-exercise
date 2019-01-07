import gzip, bz2, os

dt = {}
pylst = [x for x in os.listdir() if x.endswith('.py')]
res = sorted([(x,os.path.getsize(x)) for x in pylst], key=lambda s:s[0])

with open(res[0][0], 'rt') as f:
    data = f.read()

with gzip.open('test.gz', 'wt') as f:
    f.write(data)

with gzip.open('test.gz', 'rt') as f:
    text = f.read()
    print(text)

print('*'*50)

with bz2.open('test.bz2', 'wt') as f:
    f.write(data)

with bz2.open('test.bz2', 'rt') as f:
    text = f.read()
    print(text)
