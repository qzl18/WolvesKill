# -*- coding:utf-8 -*-
from socket import *
import sys
import getpass




class Client():
    def __init__(self,HOST="127.0.0.1",PORT=8000):
        self.s = socket(AF_INET,SOCK_DGRAM)
        self.HOST = HOST
        self.PORT = PORT
        self.ADDR = (self.HOST,self.PORT)




    def do_register(self):
        while True:
            name = input('User:')
            passwd = getpass.getpass()
            passwd1 = getpass.getpass('Again:')

            if (' ' in name ) or (" " in passwd):
                print("用户名或者密码不能有空格.")
                continue
            if passwd != passwd1:
                print("两次密码不一致")
                continue
            msg = 'R %s %s'%(name, passwd)
            #发送请求
            self.s.sendto(msg.encode(),self.ADDR)
            #等待回复
            data,addr = self.s.recvfrom(128)
            data=data.decode()
            if data == "OK":
                print("注册成功")
            elif data == "EXISTS":
                print("用户已存在")
            else:
                print("注册失败")
            return 

    def do_login(self):
        name = input('User:')
        passwd = getpass.getpass()
        msg = "L %s %s"%(name,passwd)
        self.s.sendto(msg.encode(),self.ADDR)
        data,addr = self.s.recvfrom(1024)
        data = data.decode()
        if data == "OK":
            print("登录成功")
            self.name = name
            self.login()
        else:
            print("登录失败")

    def login(self):
        while True:
            print('''
            ==============查询界面================
            |1.创建房间      2.加入房间       3.注销|
            =====================================
            ''')

            try:
                cmd = int(input("输入选项:"))
            except Exception as e:
                print("命令错误.")
                continue

            if cmd not in [1,2,3]:
                print("没有该选项.")
                continue
            elif cmd == 1:
                self.create_room()
            elif cmd == 2:
                self.join_room()
            elif cmd == 3:
                return
    def create_room(self):
        '''
        创建房间,返回房间号
        '''
        msg = "C %s"%self.name
        self.s.sendto(msg.encode(),self.ADDR)
        data,addr = self.s.recvfrom(1024)
        data = data.decode()
        l = data.split(" ")
        ##返回房间编号
        if l[0] == "room_number":
            self.room_number = int(l[1])
            print("创建的房间号是%d,快邀请好友进入房间吧!"%self.room_number)
            #显示房间
            self.in_room()

    def join_room(self):
        room_number = input("请输入要加入的房间号")
        msg = "J %s %s"%(self.name,room_number)
        self.room_number = room_number
        self.s.sendto(msg.encode(),self.ADDR)
        data,addr = self.s.recvfrom(1024)
        data = data.decode()
        if data == "OK":
            print("OK")
            self.in_room()
            #进入房间后选择位置和准备游戏
        else:
            print(data)
            return
#------------------------座位系统,暂时删除----------------------
    # def in_room(self):
    #     while True:
    #         seat_list = ["#"]*9
    #         print("""
    #         ==================================
    #         |1:%s            2:%s       3:%s  |
    #         |4:%s            5:%s       6:%s  |
    #         |7:%s            8:%s       9:%s  |
    #         |     1.开始游戏(房主) 2.准备       |     #这里需要多搞一个线程实现选择座位,暂时留着
    #         ==================================
    #         """%tuple(seat_list))
    #         data,addr = self.s.recvfrom(1024)
    #         data = data.decode().split(" ")
    #         #这里需要多搞一个线程
    #         # change_seat(self,seat)
    #         #刷新座位情况
    #         if data[0] == "change_seat":
    #             seat = int(data[1])
    #             name = data[2]
    #             seat_list[seat-1] = name


    # def change_seat(self,seat):
    #     seat = input("请选择座位:(取消座位请打#)")
    #     msg = "S %s %s"%(seat,self.name)
    #     self.s.sendto(msg.encode(),self.ADDR)
#########################################################
    def in_room(self):
        while True:
            print('''
            ===================Welcome==================
            |1.准备游戏                           2.退出 |
            ============================================
            ''')
            try:
                cmd = int(input("输入选项:"))
            except Exception as e:
                print("命令错误.")
                continue

            if cmd not in [1,2,3]:
                print("没有该选项.")
                continue
            elif cmd == 1:
                self.ready()
            elif cmd == 2:
                return

               

    def ready(self):
        msg = "G %s %s "%(self.name,self.room_number)
        self.s.sendto(msg.encode(),self.ADDR)
        data,addr = self.s.recvfrom(1024)
        data = data.decode()
        if data == "OK":
            self.start_game()


    def start_game(self):
        print("开始游戏")
        pass


            
            

#网络连接
def main():
    cl = Client()
    while True:
        print('''
        ===================Welcome==================
        |1.注册            2.登录           3.退出 |
        ============================================
        ''')

        try:
            cmd = int(input("输入选项:"))
        except Exception as e:
            print("命令错误.")
            continue

        if cmd not in [1,2,3]:
            print("没有该选项.")
            continue
        elif cmd == 1:
            cl.do_register()
        elif cmd == 2:
            cl.do_login()
        elif cmd == 3:
            cl.s.sendto(b"E",cl.ADDR)
            sys.exit("谢谢使用,bye")



if __name__ == "__main__":
    main()