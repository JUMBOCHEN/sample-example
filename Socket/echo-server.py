'''此处代码参看python cookbook3第12章'''
from socket import*
myHost = '' #此处为空字符串，默认服务器host为本机IP
myPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM) #创建socket udp
sockobj.bind((myHost, myPort)) #socket 绑定 host，port
sockobj.listen(5) #开始监听到来的客户端连接，并允许保留5个挂起的请求

while True:
	connection, address = sockobj.accept()
	print('Server connection by', address)
	while True:
		data = connection.recv(1024)
		if not data: break
		connection.send(b'Echo=>' + data)
	connection.close()