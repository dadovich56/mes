import socket
import threading

dan1 = []
ip1 = []
geb = int(input('введите порт: '))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', geb))
sock.listen()

a = input('введите ваш ник: ')

def mes_all(data, a1):
	for geg in dan1:
		if not geg==a1:
			geg.send(data)

def listen1(a1, ry):
	while True:
		data = a1.recv(2048)
		if not data:
			ip1.remove(ry)
			dan1.remove(a1)
			break
		print(data.decode('utf-8'))
		mes_all(data, a1)

def acpt():
	while True:
		a1, a2 = sock.accept()
		dan1.append(a1)
		ip1.append(a2[0])
		ry = a2[0]
		threading.Thread(target=listen1, args=(a1, ry,)).start()


def mes():
	while True:
		a3 = input('введите ваше сообщение: ')
		b = '''
'''+a+': '+a3
		if(a3=='/showip'):
			print(ip1)
		else:
			for jjej in dan1:
				jjej.send(b.encode('utf-8'))


t1 = threading.Thread(target=mes, args=())
t2 = threading.Thread(target=acpt, args=())

t1.start()
t2.start()