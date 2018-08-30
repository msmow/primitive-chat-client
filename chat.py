import client
import server
import threading


HOST1 = '192.68.43.238'
PORT1 = 4000
new_server = server.Server()

HOST2 = '192.68.43.126'
PORT2 = 4001
new_client = client.Client()