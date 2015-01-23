from socket import *
import sys


def main(argv):
    host = '127.0.0.1'
    port = 4760

    # Message to send to the server from argv
    message = str(argv[0])

    sock = socket(AF_INET, SOCK_STREAM)
    # Connect to server
    sock.connect((host, port))
    # Send message to server
    sock.send(message)
    # Receive message from server and print it to console
    received = sock.recv(1024)
    print str(received)
    # Close the socket / TCP connection
    sock.close()


if __name__ == '__main__':
    main(sys.argv[1:])