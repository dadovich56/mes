import socket
import threading

geb1 = str(input('введите хост: '))
geb2 = int(input('введите порт: '))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((geb1, geb2))

a = input('введите ваш ник: ')

def mes():
	while True:
		a3 = input('введите ваше сообщение: ')
		b = '''
'''+a+': '+a3
		sock.send(b.encode('utf-8'))

def listen():
	while True:
		data = sock.recv(2048)
		print(data.decode('utf-8'))

t1 = threading.Thread(target=mes, args=())
t2 = threading.Thread(target=listen, args=())

t1.start()
t2.start()