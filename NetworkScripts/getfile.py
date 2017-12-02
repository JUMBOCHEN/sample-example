'''
**********************一个简单的python文件服务器***********
实现客户端与服务器端逻辑，通过套接字从服务器传输任意文件到客户端；
使用一个简单的控制信息协议,而不是一个单独的套接字，用于控制和传输；
分派每个客户端请求到一个处理线程，通过分块，循环传输整个文件
***********************************************************
'''
import sys, os, time, _thread as thread
from socket import *

blksz = 1024
defaultHost = 'localhost'
defaultPort = 50007

helptext = '''
Usage...
server=> getfile.py -mode server    [-port nnn] [-host hhh|localhost]
client=> getfile.py [-mode client] -file fff [-port nnn] [-host hhh|localhost]
'''

def now():
    return time.asctime()

def parsecommandline():
    dict = {}               #put in dictionary for easy lookup
    args = sys.argv[1:]     #skip program name at front of args
    while len(args) >= 2:   #example:dict['-mode'] = 'server'
        dict[args[0]] = args[1]
        args = args[2:]
    return dict

def client(host, port, filename):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    sock.send((filename + '\n').encode())   #send remote name with dir:byte
    dropdir = os.path.split(filename[1])    #filename at end of dir path
    file = open(dropdir, 'wb')
    while True:
        data = sock.recv(blksz)             #get up to 1k at a time
        if not data: break                  #till closed on server side
        file.write(data)                    #store data in local file
    sock.close()
    file.close()
    print('client got', filename, 'at', now())

def serverthread(clientsock):
    sockfile = clientsock.makefile('r')
    filename = sockfile.readline()[:-1]
    try:
        file = open(filename, 'rb')
        while True:
            bytes = file.read(blksz)        #read/send 1k at a time
            if not bytes: break
            sent = clientsock.send(bytes)
            assert sent == len(bytes)
    except:
        print('Error downing file on server:', filename)
    clientsock.close()

def server(host, port):
    serversock = socket(AF_INET, SOCK_STREAM)   #listen on tcp/ip socket
    serversock.bind(host, port)                 #server socket in threads
    serversock.listen(5)
    while True:
        clientsock, clientaddr = serversock.accpet()
        print('Server connect by', clientaddr, 'at', now())
        thread.start_new_thread(serverthread, (clientsock,))

def main(args):
    host = args.get('-host', defaultHost)       #use args or defaults
    port = int(args.get('-port', defaultPort))   #is a string in argv
    if args.get('-mode') == 'server':
        if host == 'localhost': host = ''       #else fails remotely
        server(host, port)
    elif args.get('-file'):
        client(host, port, args['-file'])
    else:
        print(helptext)


if __name__ == '__main__':
    args = parsecommandline()
    main(args)

'''
# **********edit by ChenZuobao***********************
根据传递的命令行参数，它会调用下面两个函数中的一个：
# server函数会把每个传入的客户端请求移交到一个线程，
# 该线程可以传输请求文件字节。
# client函数发送给服务器一个文件名称，存储同名的本地文件
# 中返回的所有字节。
# 客户端和服务器之间的协议：客户端通过传递一个文件名字符串
# 到服务器来启动会话，遇到换行符终止。
# 参阅 《python编程》
'''