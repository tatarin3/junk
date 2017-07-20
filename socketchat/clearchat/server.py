import socket
import threading
import sys
import pickle
import serveroperations

class Server():
	def __init__(self, host="localhost", port=4000):

		self.clients = []
		self.wwclients = {}
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((str(host), int(port)))
		self.sock.listen(10)
		self.sock.setblocking(False)

		aceptar = threading.Thread(target=self.acceptingConns)
		procesar = threading.Thread(target=self.recievingMsgs)
		
		aceptar.daemon = True
		aceptar.start()

		procesar.daemon = True
		procesar.start()

		while True:
			msg = input('->')
			if msg == 'exit':
				self.sock.close()
				sys.exit()
			else:
				pass


	def msg_to_all(self, msg, cliente):
		for c in self.clients:
			try:
				if c != cliente and self.wwclients[c.getpeername()][0] == 2:
					c.send(msg)
			except:
				del self.wwclients[c.getpeername()]
				self.clients.remove(c)

	def acceptingConns(self):
		print("Ожидание подключений")
		while True:
			try:
				conn, addr = self.sock.accept()
				conn.setblocking(False)
				self.clients.append(conn)
				self.wwclients[conn.getpeername()] = [0,'']
			except:
				pass

	def recievingMsgs(self):
		print("Ожидание сообщений")
		while True:
			if len(self.clients) > 0:
				for c in self.clients:
					try:
						data = c.recv(1024)
						sdata = repr(data)
						print(sdata)
						print(self.wwclients)
						if data:
							if self.wwclients[c.getpeername()][0] == 2:
								self.msg_to_all(data,c)
							elif self.wwclients[c.getpeername()][0] == 0:
								if serveroperations.check_name_exists(sdata):
									found = 0
									for b in self.wwclient:
										if b[1] == sdata:
											c.send('Такой пользователь уже залогинен')
											print('Пользователь {} попытался войти под '+\
												'уже залогиненым именем'.format(c.getpeername()))
											found = 1
									if not found:
										self.wwclient[c.getpeername()] = [1, sdata]
										c.send('Вы ввели логин')
										print('Пользователь {} ввел логин'.format(c.getpeername()))
								else:
									serveroperations.create_user(sdata)
									self.wwclients[c.getpeername()] = [1,sdata]
									c.send('Вы создали учетную запись')
									print('Пользователь {} создал учетную запись'.format(c.getpeername()))
							elif self.wwclients[c.getpeername()][0] == 1:
								if serveroperations.get_user_password() == '':
									serveroperations.set_user_password(self.wwclients[c.getpeername()][1],sdata)
									self.wwclients[c.getpeername()][0] = 2
									c.send('Вы залогинились')
									print('Пользователь {} залогинился'.format(c.getpeername()))
								elif serveroperations.get_user_password(self.wwclients[c.getpeername()][1]) == sdata:
									self.wwclients[c.getpeername()][0] = 2
									c.send('Вы залогинились')
									print('Пользователь {} залогинился'.format(c.getpeername()))
								else:
									self.wwclients[c.getpeername()] = [0,'']
									c.send('Вы ввели неверный пароль')
									print('Пользователь {} разлогинился'.format(c.getpeername()))

					except:
						pass


s = Server()