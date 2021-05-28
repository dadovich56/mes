import socket
import threading

dan1 = []
ip1 = []
nicks = []
geb = int(input('введите порт: '))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', geb))
sock.listen()

a = input('введите ваш ник: ')

def mes_all(data, a1):
	for geg in dan1:
		if not geg==a1:
			geg.send(data)

def listen1(a1, ry, nick1):
	while True:
		data = a1.recv(2048)
		if not data:
			print('''
''' + nick1 + ' отключился')
			threading.Thread(target=mes_all, args=('''
''' + nick1 + ' отключился', a1,))
			nicks.remove(nick1)
			ip1.remove(ry)
			dan1.remove(a1)
			break
		print(data.decode('utf-8'))
		mes_all(data, a1)

def acpt():
	while True:
		a1, a2 = sock.accept()
		nick = a1.recv(2048)
		heshi = '''
''' + nick.decode('utf-8') + ' подключился'
		print(heshi)

		threading.Thread(target=mes_all, args=(heshi, a1,))

		nicks.append(nick.decode('utf-8'))
		dan1.append(a1)
		ip1.append(a2[0])
		ry = a2[0]
		threading.Thread(target=listen1, args=(a1, ry, nick.decode('utf-8'),)).start()


def mes():
	while True:
		a3 = input('введите ваше сообщение: ')
		b = '''
'''+a+': '+a3
		if(a3=='/showip'):
			print(ip1)
		elif(a3[0:4]=='/ban'):
			ger = int(a3[5:len(a3)]) - 1
			dan1[ger].send('''
вы были выгнаны с сервера, нажмите ctrl + c чтобы выйти'''.encode('utf-8'))
			dan1[ger].close()
		elif(a3=='/shownicks'):
			print(nicks)
		elif(a3[0:5]=='/send'):
			hyn1 = int(a3[6:len(a3)])
			a32 = input('ваше личное сообщение: ')
			fff = '''
'''+ '<личное> ' + a + ': ' + a32
			dan1[hyn1].send(fff.encode('utf-8'))
		elif(a3[0:6]=='/anon '):
			b22222 = '\n <анонимно>: '+a3[6:len(a3)]
			for jjej in dan1:
				jjej.send(b22222.encode('utf-8'))
		else:
			for jjej in dan1:
				jjej.send(b.encode('utf-8'))


t1 = threading.Thread(target=mes, args=())
t2 = threading.Thread(target=acpt, args=())

t1.start()
t2.start()
