import socket
import sys

def main(argv):
    host = '127.0.0.1'
    port = 4200

    message = str(argv[0])
    sock = socket.socket()
    sock.connect((host, port))

    #text = raw_input("Enter text to send to server")
    #while text != 'exit':
    sock.send(message)
    received = sock.recv(1024)
    print str(received)
    #text = raw_input("Enter text to send to server or 'exit' to quit")


if __name__ == '__main__':
    main(sys.argv[1:])