import socket
import threading
import sys
import pickle
import serveroperations

class Servidor():
    """docstring for Servidor"""
    def __init__(self, host="localhost", port=4000):

        self.clientes = []
        self.wwclient = {}
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((str(host), int(port)))
        self.sock.listen(10)
        self.sock.setblocking(False)

        aceptar = threading.Thread(target=self.aceptarCon)
        procesar = threading.Thread(target=self.procesarCon)

        aceptar.daemon = True
        aceptar.start()

        procesar.daemon = True
        procesar.start()

        while True:
            msg = input('->')
            if msg == 'salir':
                self.sock.close()
                sys.exit()
            else:
                pass


    def msg_to_all(self, msg, cliente):
        for c in self.clientes:
            try:
                if c != cliente and self.wwclient[c.getpeername()][0] == 2:
                    c.send(msg)
            except:
                self.clientes.remove(c)

    def aceptarCon(self):
        print("aceptarCon iniciado")
        while True:
            try:
                conn, addr = self.sock.accept()
                conn.setblocking(False)
                self.clientes.append(conn)
                self.wwclient[conn.getpeername()] = [0,'']
            except:
                pass

    def procesarCon(self):
        print("ProcesarCon iniciado")
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        data = c.recv(1024)
                        if data:
                            #если залогинин отправлять сообщения
                            if self.wwclient[c.getpeername()][0] == 2:
                                self.msg_to_all(data,c)
                            #если незалогинен принять сообщение как логин, и если он не занят присвоить этот логин, либо создать и присвоить
                            elif self.wwclient[c.getpeername()][0] == 0:
                                if serveroperations.check_name_exists(data):
                                    found = 0
                                    for b in self.wwclient:
                                        if b[1] == data:
                                            c.sendall('Vaffanculo, schemo!')
                                            found = 1
                                        if not found:
                                            self.wwclient[c.getpeername()] = [1, data]
                                else:
                                    serveroperations.create_user(data)
                                    self.wwclient[c.getpeername()] = [1, data]
                            #если статус пассвординга тогда присваивание пароля и логин, если пароль неназначен и сравнивание даты с паролем и логин если они равны
                            elif self.wwclient[c.getpeername()][0] == 1:
                                if serveroperations.get_user_password(self.wwclient[c.getpeername()][1]) == '0':
                                    serveroperations.set_user_password(self.wwclient[c.getpeername()][1], data)
                                    self.wwclient[c.getpeername()][0] = 2
                                elif serveroperations.get_user_password(self.wwclient[c.getpeername()][1]) == data:
                                    self.wwclient[c.getpeername()][0] = 2
                                else:
                                    self.wwclient[c.getpeername()] = [0,'']


                    except:
                        pass


s = Servidor()
