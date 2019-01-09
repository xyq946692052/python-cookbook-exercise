from socketserver import StreamRequestHandler, TCPServer

class EchoHandler(StreamRequestHandler):
    def handle(self):
        print('Got connection from ', self.client_address)
        for line in self.rfile:
            self.wfile.write(line)


if __name__ == '__main__':
    serv = TCPServer(('', 20001), EchoHandler)
    serv.serve_forever()
