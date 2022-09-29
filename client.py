import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9090))

while True:
    msg = input('Введите сообщение: ')
    sock.send(msg.encode())
    if msg == 'exit':
        break

    data = sock.recv(1024)
    print(data.decode())

sock.close()
