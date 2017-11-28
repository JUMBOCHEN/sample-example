'''
**********************一个简单的python文件服务器***********
实现客户端与服务器端逻辑，通过套接字从服务器传输任意文件到客户端；
使用一个简单的控制信息协议；
分派每个客户端请求到一个处理线程，通过分块，循环传输整个文件
***********************************************************
'''
import os, sys, time, _thread as thread
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
    dict = {}
    args = sys.argv[1:]
    while len(args) >=2:
        dict[args[0]] = args[1]
        args = args[2:]
    return dict

def client(host, port, filename):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host,port))
    sock.send((filename + '\n').encode())
    dropdir = os.path.split(filename[1])
    file = open(dropdir, 'wb')
    while True:
        data = sock.recv(blksz)
        if not data:break
        file.write(data)
    sock.close()
    file.close()
    print('client got', filename, 'at', now())

def serverthread(clientsock):
    pass

def server(host, port):
    pass

def main(args):
    pass

if __name__ == '__main__':
    args = parsecommandline()
    main(args)