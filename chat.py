import client
import server

HOST1 = '192.68.43.238'
PORT1 = 4000

HOST2 = '192.68.43.126'
PORT2 = 4001


def main():
	new_server = server.Server()
	new_client = client.Client()
	new_server.run()


if __name__ == '__main__':
	main()