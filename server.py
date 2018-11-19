# -*-coding:utf-8 -*-
'''
这是狼人杀服务端
https://blog.csdn.net/ICanDo_It/article/details/53174582
'''
from socket import *
from multiprocessing import *
from threading import Thread
import struct

HOST = "127.0.0.1"
PORT = 8888
ADDR = (HOST,PORT)

def do_request(sockfd):
    st = struct.Struct()

def main():
    #创建套接字并链接服务器
    sockfd = socket(AF_INET,SOCK_DGRAM)
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)

    data,addr = sockfd.recvfrom(1024)
    
    #接收客户端请求进行处理请求
    
    # do_request(sockfd)
    


if __name__ == "__main__":
    main()

