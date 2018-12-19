import textwrap

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

print(textwrap.fill(s, 70))

print('*'*50)

print(textwrap.fill(s, 40))

print('*'*50)

print(textwrap.fill(s, 40, initial_indent='     '))

print('*'*50)

print(textwrap.fill(s, 40, subsequent_indent='    '))

print('*'*50)

import os
print(os.get_terminal_size().columns)
