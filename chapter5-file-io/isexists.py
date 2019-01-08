import os

print(os.path.exists('/etc/abc'))

print(os.path.exists('/usr/bin'))

print(os.path.isfile('/usr/bin/yum'))

print(os.path.isdir('/usr/bin'))

print(os.path.islink('/usr/local/bin/python3'))

print(os.path.realpath('/usr/local/bin/python3'))

print(os.path.getsize('/usr/local'))

print(os.path.getmtime('/etc/passwd'))

import time
print(time.ctime(os.path.getmtime('/etc/passwd')))

