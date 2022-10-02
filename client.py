import socket

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9090))

while True:
    msg = input('Введите сообщение: ')
    if msg == 'exit':
        break
    sock.send(msg.encode())
    if msg == 'server off':
        break

    data = sock.recv(1024)
    print(data.decode())
sock.close()


