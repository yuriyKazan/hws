import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))
