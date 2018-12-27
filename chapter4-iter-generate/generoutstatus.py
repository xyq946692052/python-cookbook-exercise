#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from collections import deque
import os

class Linehistory:
    def __init__(self, lines, history=3):
        self.lines = lines
        self.history = deque(maxlen=history)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


if __name__ == '__main__':
  
    flst = os.listdir(os.getcwd())
    with open(flst[0]) as f:
        lines = Linehistory(f)
        for line in lines:
            if 'print' in line:
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno, hline), end='')
