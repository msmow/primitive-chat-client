import socket

class Client():

    def __init__(self, host='127.0.0.1', port=4000):
        self.HOST = host  # The server's hostname or IP address
        self.PORT = port  # The port used by the server

    def connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.HOST, self.PORT))

    def run(self):
        while True:
            data = input()
            self.s.sendall(data.encode('utf-8'))

    def close(self):
        self.s.close()