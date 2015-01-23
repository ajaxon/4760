from socket import *


def main():
    host = '127.0.0.1'
    port = 4760

    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind((host, port))

    print "Server running"

    while True:
        data, client = server_socket.recvfrom(1024)
        server_socket.sendto("You said: " + str(data), client)


if __name__ == '__main__':
    main()