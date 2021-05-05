import socket
import threading

dan1 = []
ip1 = []
geb = int(input('введите порт: '))
gegegeb = int(input('введите количество подключений: '))

if(gegegeb>5):
	print('нельзя больше 5 подключений')
else:
	sock = socket.socket(socket.AF_INET, 			socket.SOCK_STREAM)
	sock.bind(('127.0.0.1', geb))
	sock.listen(gegegeb)
	
	a = input('введите ваш ник: ')
	print('ожидание подключений...')
	a1, a2 = sock.accept()
	dan1.append(a1)
	ip1.append(a2[0])
	if(gegegeb>1):
		a4, a5 = sock.accept()
		dan1.append(a4)
		ip1.append(a5[0])
		if(gegegeb>2):
			a6, a7 = sock.accept()
			dan1.append(a6)
			ip1.append(a7[0])
			if(gegegeb>3):
				a8, a9 = sock.accept()
				dan1.append(a8)
				ip1.append(a9[0])
				if(gegegeb>4):
					a10, a11 = sock.accept()
					dan1.append(a10)
					ip1.append(a11[0])
	
	def mes():
		while True:
			a3 = input('введите ваше сообщение: ')
			b = '''
'''+a+': '+a3
			if(a3=='/showip'):
				print(ip1)
			else:
				a1.send(b.encode('utf-8'))
				if(gegegeb>1):
					a4.send(b.encode('utf-8'))
					if(gegegeb>2):
						a6.send(b.encode('utf-8'))
						if(gegegeb>3):
							a8.send(b.encode('utf-8'))
							if(gegegeb>4):
								a10.send(b.encode('utf-8'))
	
	def listen():
		while True:
			data = a1.recv(2048)
			print(data.decode('utf-8'))
	
	def listen2():
		while True:
			data2 = a4.recv(2048)
			print(data2.decode('utf-8'))
	
	def listen3():
		while True:
			data3 = a6.recv(2048)
			print(data3.decode('utf-8'))
	
	def listen4():
		while True:
			data4 = a8.recv(2048)
			print(data4.decode('utf-8'))
	
	def listen5():
		while True:
			data5 = a10.recv(2048)
			print(data5.decode('utf-8'))
	
	t1 = threading.Thread(target=mes, args=())
	t2 = threading.Thread(target=listen, args=())
	t3 = threading.Thread(target=listen2)
	t4 = threading.Thread(target=listen3)
	t5 = threading.Thread(target=listen4)
	t6 = threading.Thread(target=listen5)
	
	t1.start()
	t2.start()
	if(gegegeb>1):
		t3.start()
		if(gegegeb>2):
			t4.start()
			if(gegegeb>3):
				t5.start()
				if(gegegeb>4):
					t6.start()