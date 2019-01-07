with open('audi.jpg', 'rb') as f:
    data = f.read()
    #print(data, end='\n')

with open('audi.txt', 'wb') as f:
    f.write(b'Hello audi')


for c in 'Hello World':
    print(c, end=' ')


for c in b'Hello World':
    print(c, end=' ')


with open('yum', 'rb') as f:
    data = f.read()
    text = data.decode('utf-8')
    print(text)


with open('test.bin', 'wb') as f:
    text = 'Hello world'
    f.write(text.encode('utf-8'))


import array
nums = array.array('i', [1, 2, 3, 4])
with open('data.bin', 'wb') as f:
    f.write(nums)

with open('data.bin', 'rb') as f:
    data = f.read()
    print(data)


b = array.array('i', [0,0,0,0,0,0,0,0])
with open('data.bin', 'rb') as f:
    f.readinto(b)
