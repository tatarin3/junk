import socket
import sys
import serveroperations
from _thread import *


def server_listen(host,port):
	listaddr = []
	'''Creating server with host and port and listening'''
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	while True:
		try:
			s.bind((host,port))
		except socket.error as e:
			print(str(e))


	s.listen(10)
	print('Waiting for connection')


	def connected_client(conn,address):

		conn.send(str.encode('Welcome, to the cheapchat v0.1a'))

		while True:

			data = conn.recv(2048) #recieve data in bytecode
			if not data:
				break
			if check_login_status(address):
				conn.sendall(str.encode(get_user_name(address)+": "+data))
			else:
				reply = serveroperations.server_get(data.decode('utf-8'),address)
				conn.sendall(str.encode(reply))

		serveroperations.delete_address_from_user(address)
		serveroperations.set_user_status(address,0)
		conn.close()



	while True:
		conn, addr = s.accept() #New connection WHY IT WORK JUST ONCE???
		print('Connected to: ' + addr[0] + ':' + str(addr[1]))
		address = str(addr[0]) + str(addr[1])
		start_new_thread(connected_client(conn,address))
