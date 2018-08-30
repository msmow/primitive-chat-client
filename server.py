import socket

class Server():

    def __init__(self, host='127.0.0.1', port=4000):
        self.HOST = host
        self.PORT = port  # Port to listen on (non-privileged ports are > 1023)

    def listen(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.HOST, self.PORT))
        self.s.listen()

    def accept(self):
        self.conn, self.addr = self.s.accept()

    def run(self):
        with self.conn:
            print('Connected by', self.addr)
            while True:
                data = self.conn.recv(1024)
                if data:
                    print(data.decode('utf-8'))