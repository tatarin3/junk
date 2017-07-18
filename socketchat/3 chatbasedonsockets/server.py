import serversocket

host = "localhost"
port = 7753

if __name__ == '__main__':
	#host = input("Input your server's host: ")
	#port = int(input("Input your server's port: "))
	serversocket.server_listen(host,port)
