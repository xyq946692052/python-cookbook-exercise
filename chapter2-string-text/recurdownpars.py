#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
Topic: 下降解析器
DESC: 
"""
import re
import collections

#Token
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(P<MINUS>-)'
TIMES = r'(P<TIMES>\*)'
DIVIDE = r'(P<DIVIDE>/)'
LPAREN = r'(P<LPAREN>\()'
RPAREN = r'(P<RPAREN>\))'
WS = r'(P<ES>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES, DIVIDE, LPAREN, RPAREN, WS]))

#Tokenizer
Token = collections.namedtuple('Token', ['type', 'value'])

def generate_token(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok


#paser
class ExpressionEvaluator:
    def parse(self, text):
        self.tokens = generate_token(text)
        self.tok = None
        self.nexttok = None
        self._advance()
        return self.expr()

    def _advance(self):
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    def _accept(self, toktype):
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def expect(self, toktype):
        if not self._accept(toktype):
            raise SyntaxError('Excepted '+toktype)

    def expr(self):
        exprval = self.term()
        while self._accept('PLUS') or self._accept("MINUS'):
            op = self.tok.type
            right = self.term()




