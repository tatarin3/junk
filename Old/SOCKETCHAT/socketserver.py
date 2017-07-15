import socket
def server():
    #creating socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #binding there
    address = '127.0.0.1'
    port = 7000
    sock.bind((address,port))
    #listenfunc
    print('Listening')
    sock.listen(5)
    while 1:
        conn,addr = sock.accept()
        print('Connected to ',addr)

        while 1:
            #get data from connection
            data = conn.recv(1024)
            if not data: break # if data == 0 close conn
            print('Reveived ',data)
            #do something with it
            conn.send(data)

        conn.close()
