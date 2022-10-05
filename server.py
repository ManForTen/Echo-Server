import socket

f = open('log.txt', 'w')

breaker = 0

TYPE = socket.AF_INET
PROTOCOL = socket.SOCK_STREAM

sock = socket.socket(TYPE,PROTOCOL)
sock.bind(('', 9090))
sock.listen(1)
f.write('Успешное подключение!')
print('Успешное подключение!')
print('Введите server off, для отключения сервера.')

while True:
	conn, addr = sock.accept()
	f.write('Подключен:' + addr[0] + '\n')
	print('Подключен:', addr)
	while True:
		f.write('Прием данных:' + '\n')
		print('Прием данных:')
		try:
			data = conn.recv(1024)
		except (ConnectionAbortedError, ConnectionResetError):
			f.write('Ошибка!' + '\n')
			print('Ошибка!')
		msg = data.decode()
		f.write(msg + '\n')
		print(msg)
		if msg == 'server off':
			breaker += 1
			break
		if not data:
			break
		conn.send(data)

	conn.close()
	f.write('Отключение клиента!' + '\n')
	print('Отключение клиента!')
	if breaker == 1:
		f.write('Отключение сервера!' + '\n')
		print('Отключение сервера!')
		break

f.close()