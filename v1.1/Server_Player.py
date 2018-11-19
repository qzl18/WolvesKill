'''
player属性:
服务器的套接字对象
身份
是否存活
是否为警长
个人位置编号
客户端地址
用户名
房间号
'''
import Sever_Room as sr
 
class Player():
    def __init__(self,s,addr,name):
        self.s = s
        self.identity = None
        self.alive = True
        self.police = False
        self.number = None
        self.addr = addr
        self.name = name
        self.room = None
        

    def create_room(self):
        self.room = sr.Room(self)
        b = self.room.create()

        if b ==True:
        #返回房间对象
            msg = "room_number %s" %str(self.room.room_number)
            self.s.sendto(msg.encode(),self.addr)
            return self.room

    def join_room(self,room):
        self.room = room
        return True
    
    def show(self):
        print("#####################Player##################")
        print("self.s=",self.s)
        print("self.identity=",self.identity)
        print("self.alive= ",self.alive )
        print("self.police=",self.police )
        print("self.number=",self.number)
        print("self.addr=",self.addr)
        print("self.name=", self.name)
        print("self.room=",self.room)