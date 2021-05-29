import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 65432
BUFFER_SIZE = 1024

SERVER_SOCKET = (SERVER_IP, SERVER_PORT)
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind(SERVER_SOCKET)
print('UDP server up and listening on {} port {}'.format(*SERVER_SOCKET))

while True:
    print('Waiting for a connection')
    try:
        while True:
            bytesAddressPair = UDPServerSocket.recvfrom(BUFFER_SIZE)
            if bytesAddressPair:
                message = bytesAddressPair[0].decode("utf-8")
                address = bytesAddressPair[1]
                print("Message from Client:'{}'".format(message))
                print("Client IP:{}, Port:{}".format(*address))
                UDPServerSocket.sendto(str.encode(message), address)
            else:
                print('No data from:{}')
                break

    finally:
        if UDPServerSocket:
            UDPServerSocket.close()
