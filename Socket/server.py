import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9990))
while True:
	data,addr = s.recvfrom(1024)
	print('Receice from %s:%s.'%addr)
	s.sendto(b'hello, %s!'%data,addr)
	print(data)
	