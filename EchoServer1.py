from socket import *


def main():
    # Host machine address server is running on
    host = '127.0.0.1'
    # Port used
    port = 4760

    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((host, port))

    server_socket.listen(2)
    print "Server running"

    while True:

        c, addr = server_socket.accept()
        print "Connection " + str(addr)
        data = c.recv(1024)
        if data:
            print str(data)
            c.send("You said: " + str(data))

        c.close()


if __name__ == '__main__':
    main()