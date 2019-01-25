import hmac
import os
from socket import socket, AF_INET, SOCK_STREAM


secret_key = b'peekaboo'


def client_authenticate(connection, secret_key):
    '''
    Authenticate client to a remote service.
    connection represents a network connection.
    secret_key is a key known only to both client/server.
    '''
    message = connection.recv(32)
    hash = hmac.new(secret_key, message)
    digest = hash.digest()
    connection.send(digest)



def server_authenticate(connection, secret_key):
    '''
    Request client authentication.
    '''
    message = os.urandom(32)
    connection.send(message)
    hash = hmac.new(secret_key, message)
    digest = hash.digest()
    response = connection.recv(len(digest))
    return hmac.compare_digest(digest,response)


s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 18001))
client_authenticate(s, secret_key)
s.send(b'hello world')
resp = s.recv(1024)
