import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
print('Успешное подключение!')
print('Введите server off, для отключения сервера.')
conn, addr = sock.accept()
print(addr)
msg = ''

while True:
	print('Прием данных:')
	try:
		data = conn.recv(1024)
	except (ConnectionAbortedError, ConnectionResetError):
		print('Ошибка!')

	msg = data.decode()
	print(msg)
	if msg == 'server off':
		break
	if not data:
		break

	conn.send(data)



conn.close()
print('Отключение клиента!')