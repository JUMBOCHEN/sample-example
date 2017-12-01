from socket import *

host = '127.0.0.1' # 这是客户端的电脑的ip
port = 5500 #接口选择大于10000的，避免冲突
bufsize = 1024  #定义缓冲大小

addr = (host, port) # 元祖形式
udpClient = socket(AF_INET, SOCK_DGRAM) #创建客户端
while True:
    data = input('>>> ')
    if not data:
        break

    data = data.encode(encoding="utf-8")
    udpClient.sendto(data, addr) # 发送数据
    data,addr = udpClient.recvfrom(bufsize) #接收数据和返回地址
    print(data.decode(encoding="utf-8"), 'from', addr)

udpClient.close()