import socket, select, serveroperations

UNREGISTERED = 0
LOGGING = 1
PASSWORDING = 2
LOGGED_IN = 3

clients = {}
counter = 1

# Tcp Chat server
 
#Function to broadcast chat messages to all connected clients
def broadcast_data (sock, message):
    #Do not send the message to master socket and the client who has send us the message
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock and clients[sock.getpeername()][0] == LOGGED_IN:
            try :
                socket.sendall(message)
            except :
                # broken socket connection may be, chat client pressed ctrl+c for example
                socket.close()
                CONNECTION_LIST.remove(socket)
 
     
# List to keep track of socket descriptors
CONNECTION_LIST = []
RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
PORT = 7753
 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# this has no effect, why ?
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("0.0.0.0", PORT))
server_socket.listen(10)

# Add server socket to the list of readable connections
CONNECTION_LIST.append(server_socket)

print "Chat server started on port " + str(PORT)

while 1:
	# Get the list sockets which are ready to be read through select
	read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])

	for sock in read_sockets:
		#New connection
		if sock == server_socket:
			# Handle the case in which there is a new connection recieved through server_socket
			sockfd, addr = server_socket.accept()
			clients[addr] = [UNREGISTERED, 'Guest%s' % (counter)]
			counter += 1
			CONNECTION_LIST.append(sockfd)
			print "Client (%s) connected" % (addr[1])
		 
		#Some incoming message from a client
		else:
			# Data recieved from client, process it
			try:
				#In Windows, sometimes when a TCP program closes abruptly,
				# a "Connection reset by peer" exception will be thrown
				data = sock.recv(RECV_BUFFER)
				if data:
					if clients[sock.getpeername()][0] == LOGGED_IN:
						broadcast_data(sock, "\r" + '<' + str(clients[sock.getpeername()][1]) + '> ' + data)
					elif clients[sock.getpeername()][0] == UNREGISTERED:
						if serveroperations.check_name_exists(data) :
							found = 0
							for c in clients:
								if c[1] == data:
									sock.sendall('Vaffanculo, schemo!')
									found = 1
							if not found:
								client[sock.getpeername()] = [PASSWORDING, data]
						else:
							serveroperations.create_user(data)
							client[sock.getpeername()] = [PASSWORDING, data]
					elif clients[sock.getpeername()] == PASSWORDING:
						if serveroperations.get_user_password() == data :
							clients[sock.getpeername()] = LOGGED_IN
							broadcast_data(sock, "Client (%s) has entered the room." % clients[sock.getpeername()][1])
						else:
							sock.sendall('Incorrect password.')
			except:
				if clients[sock.getpeername()][0] == LOGGED_IN:
					broadcast_data(sock, "Client (%s, %s) is offline" % clients[sock.getpeername()][1])
				print "Client (%s, %s) is offline" % addr
				sock.close()
				CONNECTION_LIST.remove(sock)
				continue
     
server_socket.close()