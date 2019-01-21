# /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File  : rpctest.py
@Author: Kevin Xie
@Date  : 2019/01/21
@Desc  : XXX
'''
import pickle
import json
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


class RPCProxy:
    def __init__(self, connection):
        self._connection = connection

    def __getattr__(self, name):
        def do_rpc(*args, **kwargs):
            self._connection.send(json.dumps(name, args, kwargs))
            result = json.loads(self._connection.recv())
            return result
        return do_rpc


from multiprocessing.connection import Listener
from threading import Thread
#from .rpctest import RPCHandler

def rpc_server(handler, address, authkey):
    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        t = Thread(target=handler.handler_connection, args=(client,))
        t.daemon = True
        t.start()


# some remote functions
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

# Register with a handler
handler = RPCHandler()
handler.register_function(add)
handler.register_function(sub)

# Run the server
rpc_server(handler, ('localhost', 17000), authkey=b'peekaboo')
