# /usr/bin/env python3
# -*- coding: utf-8 -*-
from multiprocessing.connection import Client
from . import rpctest

c = Client(('localhost', 17002),authkey=b'peekaboo')
proxy = rpctest.RPCProxy(c)

res = proxy.add(2,3)
print(res)

