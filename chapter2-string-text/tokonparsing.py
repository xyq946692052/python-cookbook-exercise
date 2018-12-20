import re
from collections import namedtuple

text = 'foo = 23 + 42 * 10'
tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

NAME = r'(?P<NAME>[a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIME>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

def generate_token(pat, text):
    Token = namedtuple('Token',['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

for tok in generate_token(master_pat, text):
    print(tok)
 
tokens = (tok for tok in generate_token(master_pat, text) if tok.type !='WS')
for tok in tokens:
    print(tok)
