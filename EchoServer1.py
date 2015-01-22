from socket import *


def main():
    host = '127.0.0.1'
    port = 4200

    sock = socket()
    sock.bind((host, port))

    sock.listen(2)
    print "Server running"
    c, addr = sock.accept()
    print "Connection " + str(addr)

    while True:
        data = c.recv(1024)
        if data:
            print str(data)
            c.send("You said: " + str(data))
        else:
            break
    c.close()


if __name__ == '__main__':
    main()