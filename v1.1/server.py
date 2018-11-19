# -*- coding:utf-8 -*-
'''
Author:zhanghaoyu
modules:pymysql
This is a game project for AID1808 
'''
from socket import *
import pymysql
import os,sys
from threading import Thread
import Server_Player
from multiprocessing import Process 
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)
p_dict = {}
#处理僵尸进程
def zombie():
        os.wait()



#网络搭建
def main():
    server = Server(HOST,PORT)
    while True:
        #判断是否创建子进程
        data,addr = server.s.recvfrom(128)
        data=data.decode()
        print(addr,":",data)
        if not data or data[0] == "E":
            server.s.close()
            sys.exit()
        elif data[0] =="R":
            server.do_register(addr,data)
        elif data[0] =="L":
            server.do_login(addr,data)
        elif data[0] =="C":
            p = Process(target= do_child_process,args=(server.s,addr,data))
            p.setDaemon =True
            p.start()

            p_dict[p.pid]=p
            print("Pdict = ",p_dict)

        else:
            #向子进程发送数据,发一条关闭一次本地套接字
            for i in p_dict:
                if int(data.split(" ")[2])==i:
                    x = socket(AF_UNIX,SOCK_DGRAM)
                    x.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
                    f_name = "./socket/x_%d"%i
                    L = data.split(" ")
                    L[2:2] = (addr[0],str(addr[1]))
                    print(L)
                    data = " ".join(L)
                    print(data)
                    # f = open(f_name,"wb")
                    # f.close()

                    x.sendto(data.encode(),f_name)
                    x.close()
            

#创建本地套接字,进程间通信
def Unix_socket(path):
    sockfd = socket(AF_UNIX,SOCK_DGRAM)
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    sockfd.bind(path)
    return sockfd

def do_child_process(s,addr,data):
    #创建本地套接字文件
    f_name = "./socket/x_%d"%int(os.getpid())

    x = Unix_socket(f_name)

    #########这里必须用IO多路复用阻塞,否则会不断循环
    while True:
        print("child_process:",data)

        L = data.split(" ")
        name = L[1]

        ########判断请求#################
        if data[0]=="C":
            # C name
            player = Server_Player.Player(s,addr,name)
            #记录房间对象
            room = player.create_room()
            #自动加入了房间
            room.show()
            player.show()

        elif data[0]=="J":
            # "J name HOST PORT room_number
            print("child_process:",data)
            room_number = L[4]
            addr = (L[2],int(L[3]))
            player = Server_Player.Player(s,addr,name)
            a =  room.join(player)
            b = player.join_room(room)
            print(a,b)
            if a ==True and b ==True:
                s.sendto(b'OK',addr)
            room.show()
            player.show()

        elif data[0]=="G":
            room.start_game() 
        
        data,f = x.recvfrom(1024)
        data = data.decode() 
          

          


class Server():
    def __init__(self,HOST ,PORT ):
        #创建数据库连接
        self.db = pymysql.connect('127.0.0.1','root','123456','WolvesKill')
        #创建套接字
        self.HOST = HOST
        self.PORT = PORT
        self.ADDR = (self.HOST,self.PORT)

        self.s = socket(AF_INET,SOCK_DGRAM)
        self.s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.s.bind(self.ADDR)







    def do_register(self,addr,data):
        l = data.split(" ")
        name = l[1]
        passwd = l[2]
        cursor = self.db.cursor()
        sql = "select * from user where name = '%s'"%name
        cursor.execute(sql)
        r = cursor.fetchone()
        if r != None:
            self.s.sendto(b"EXISTS",addr)
            return
        #插入用户
        sql = "insert into user (name, passwd) values ('%s','%s')"%(name,passwd)
        try:
            cursor.execute(sql)
            self.db.commit()
            self.s.sendto(b'OK',addr)
        except:
            self.db.rollback()
            self.s.sendto(b"FAIL",addr)

    def do_login(self,addr,data):
        l = data.split(" ")
        name = l[1]
        passwd = l[2]
        cursor = self.db.cursor()
        sql = "select * from user where name = '%s' and passwd = '%s'"%(name,passwd)
        cursor.execute(sql)
        r = cursor.fetchone()
        if r ==None:
            self.s.sendto(b'FAIL',addr)
        else:
            self.s.sendto(b'OK',addr)




if __name__ == "__main__":
    main()