import io

s = io.StringIO()
s.write('Hello World')
print('This is a test. ', file=s)
print(s.getvalue())

s2 = io.StringIO('1234567890abc')
print(s2.read(4))
print(s2.read())


s3 = io.BytesIO()
s3.write(b'Hello python')
print(s3.getvalue())

