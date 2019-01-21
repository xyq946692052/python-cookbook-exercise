# /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File  : rpctest.py
@Author: Kevin Xie
@Date  : 2019/01/21
@Desc  : XXX
'''
import pickle
class RPCHandler:
    def __init__(self):
        self._functions = {}

    def register_function(self, func):
        self._functions[func.__name__] = func

    def handler_connection(self, connection):
        try:
            while True:
                # receive a message
                func_name, args, kwargs = pickle.loads(connection.recv())
                # run the RPC and send a response
                try:
                    r = self._functions[func_name](*args, **kwargs)
                    connection.send(pickle.dumps(r))
                except Exception as e:
                    connection.send(pickle.dumps(e))
        except EOFError:
            pass
