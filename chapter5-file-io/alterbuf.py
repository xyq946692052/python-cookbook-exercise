import os.path

def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

with open('test.gz', 'wb') as f:
    f.write(b'Hello xyq')

buf = read_into_buffer('test.gz')
print(buf)
print(buf[0:5])
