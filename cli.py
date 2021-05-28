import socket
import threading

geb1 = str(input('введите хост: '))
geb2 = int(input('введите порт: '))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((geb1, geb2))

a = input('введите ваш ник: ')
sock.send(a.encode('utf-8'))

def mes():
	while True:
		if not sock:
			break
		a3 = input('введите ваше сообщение: ')
		if(a3[0:6]=='/anon '):
			b22222 = '\n <анонимно>: '+a3[6:len(a3)]
			sock.send(b22222.encode('utf-8'))
		else:
			b = '''
'''+a+': '+a3
			sock.send(b.encode('utf-8'))

def listen():
	while True:
		data = sock.recv(2048)
		dedeg = '''
вы были выгнаны с сервера, нажмите ctrl + c чтобы выйти'''
		if not data:
			print('''
''' + 'сервер закрыт, нажмите ctrl + c чтобы выйти')
			break
		elif(data.decode('utf-8')==dedeg):
			print(data.decode('utf-8'))
			sock.close()
			break
		else:
			print(data.decode('utf-8'))

t1 = threading.Thread(target=mes, args=())
t2 = threading.Thread(target=listen, args=())

t1.start()
t2.start()
