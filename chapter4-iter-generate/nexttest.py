import os

flst = os.listdir()

with open(flst[0]) as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass

print('*'*50)

with open(flst[0]) as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')
   
