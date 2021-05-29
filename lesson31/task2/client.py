import socket
from lesson31.task2.caesar_cipher import decrypt

HOST = '127.0.0.1'
PORT = 65432
BUFFER_SIZE = 1024

data = ''
key = 0
while data != 'STOP':
    incoming_data = input('Enter message: ')
    if incoming_data in ('stop', 'STOP'):
        message = incoming_data
    else:
        key = input('Enter key: ')
        message = key + incoming_data
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(message.encode())
        data_received = s.recv(BUFFER_SIZE).decode()
        if data_received:
            print('Received message:', data_received)
            print('Decrypting...')
            data = decrypt(data_received, int(key)).upper()
        else:
            break

    print('Received', repr(data))
