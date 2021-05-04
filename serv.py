import socket
import threading

geb = int(input('введите порт: '))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', geb))
sock.listen(2)

a = input('введите ваш ник: ')
a1, a2 = sock.accept()

def mes():
	while True:
		a3 = input('введите ваше сообщение: ')
		b = '''
'''+a+': '+a3
		a1.send(b.encode('utf-8'))

def listen():
	while True:
		data = a1.recv(2048)
		print(data.decode('utf-8'))

t1 = threading.Thread(target=mes, args=())
t2 = threading.Thread(target=listen, args=())

t1.start()
t2.start()