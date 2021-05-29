import socket
from lesson31.task2.caesar_cipher import encrypt

SERVER_IP = '127.0.0.1'
SERVER_PORT = 65432
BUFFER_SIZE = 1024

SERVER_SOCKET = (SERVER_IP, SERVER_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('starting up on {} port {}'.format(*SERVER_SOCKET))
sock.bind(SERVER_SOCKET)

sock.listen(1)

stop = ''
connection = None
try:
    while stop != 'STOP':
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        print('connection from', client_address)

        while True:
            encrypted_data = connection.recv(BUFFER_SIZE)
            data = encrypted_data.decode()
            print('received {!r}'.format(data))
            if data:
                if data in ('stop', 'STOP'):
                    stop = data.upper()
                    break
                key = int(data[0])
                message = data[1:]
                print('Encrypting and sending data back to the client')
                encrypted_data = encrypt(message, key)
                connection.sendall(encrypted_data.encode())
            else:
                print('no data from', client_address)
                break

        print(stop)

finally:
    if connection:
        connection.close()
