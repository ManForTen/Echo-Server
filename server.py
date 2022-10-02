import socket

breaker = 0

TYPE = socket.AF_INET
PROTOCOL = socket.SOCK_STREAM

sock = socket.socket(TYPE,PROTOCOL)
sock.bind(('', 9089))
sock.listen(1)

print('Успешное подключение!')
print('Введите server off, для отключения сервера.')

while True:
	conn, addr = sock.accept()
	print('Подключен:', addr)
	while True:
		print('Прием данных:')
		try:
			data = conn.recv(1024)
		except (ConnectionAbortedError, ConnectionResetError):
			print('Ошибка!')
		msg = data.decode()
		print(msg)
		if msg == 'server off':
			breaker += 1
			break
		if not data:
			break
		conn.send(data)

	conn.close()
	print('Отключение клиента!')
	if breaker == 1:
		print('Отключение сервера!')
		break