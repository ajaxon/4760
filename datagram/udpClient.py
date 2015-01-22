import socket

def main():
	host = '127.0.0.1'
	port = 4200


	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# No connection created

	text = raw_input("Enter text to send to server")
	
	sock.sendto(text,(host,port))
	received = sock.recvfrom(1024)
	print str(received)
		#ext = raw_input("Enter text to send to server or 'exit' to quit")
	sock.close()


if __name__ =='__main__':
	main()