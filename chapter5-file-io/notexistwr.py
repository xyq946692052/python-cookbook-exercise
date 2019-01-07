try:
    with open('audi.txt', 'xt') as f:
        f.write(b'hello xyq')
except:
    print('file exist!')
