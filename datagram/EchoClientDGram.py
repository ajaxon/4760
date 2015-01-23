from socket import *
import sys


def main(argv):
    host = '127.0.0.1'
    port = 4760

    # Message to send to the server from argv
    message = str(argv[0])

    client_socket = socket(AF_INET, SOCK_DGRAM)

    # Send message to server
    client_socket.sendto(message, (host, port))
    # Receive message from server and print it to console
    return_message, server = client_socket.recvfrom(1024)
    print return_message
    # Close the socket / TCP connection
    client_socket.close()


if __name__ == '__main__':
    main(sys.argv[1:])