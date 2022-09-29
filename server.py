import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)
conn, addr = sock.accept()
print(addr)

msg = ''

while True:
	print('Прием данных')
	try:
		data = conn.recv(1024)
	except (ConnectionAbortedError):
		print('Ошибка!')
	msg = data.decode()
	print(msg)
	if msg == 'shutdown':
		break
	if not data:
		break

	conn.send(data)



conn.close()