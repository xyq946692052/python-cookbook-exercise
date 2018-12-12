import os

filename = os.listdir('../chapter2-string-text/')
print(filename)

print([name for name in filename if name.startswith('math')])
print([name for name in filename if name.endswith('.py')])

print(any(name.endswith('.py') for name in filename))


