from socekt import *
import multiprocessing as mp
import os,sys
import struct


HOST = "127.0.0.1"
PORT = 8888
ADDR = (HOST,PORT)
#打包发送
def do_pack(request,ob)
    len_ob = len(ob)
    st = struct.Struct("s%ds")
    return st.pack(request,ob)


#登录
def signup(tcp_sockfd):
    username = input("请输入账号")
    password = input("请输入密码")
    str_username_password = username+"#"+password
    #signup为登录请求符
    msg = do_pack('signup',str_username_password)
    data1 = tcp_sockfd.send(msg)
    data2 = tcp_sockfd.recv(1024)
    if data2.decode()=="OK":
        print("登录成功")
        return 
    else:
        print(data2.decode())

#注册
def signin(tcp_sockfd):
    while True:
        username = input("请输入账号")
        #signin_username为注册请求符_用户名
        msg = do_pack('signin_username',username)
        data1 = tcp_sockfd.send(msg)
        data2 = tcp_sockfd.recv(1024)
        print('From server:',data2.decode())
        if data2.decode() == "OK":
            while True:
                password = input("请输入密码")
                password2 = input("请确认密码")
                if password == password2:
                    #signin_password为注册请求符_密码
                    msg = do_pack('signin_password',password)
                    data1 = tcp_sockfd.send(msg)
                    data2 = tcp_sockfd.recv(1024)
                    if data2.decode()== "OK":
                        print("注册成功请登录")
                        return 
                else:
                    print("两次密码不一致请重新输入密码")
                    continue
        else:
            print('请重新输入账号:')
            continue




def do_sign(tcp_sockfd):
    choice = input("        登录(1)         注册(2)")
    if choice == "2":
        #注册
        signin(tcp_sockfd)
    #登录
    signup(tcp_sockfd)
    





def main():
    #创建套接字并链接服务器
    tcp_sockfd = socket()
    tcp_sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    
    tcp_sockfd.connect(ADDR)

    #注册登录  tcp
    do_sign(tcp_sockfd)
    #选择房间  tcp
    #开始游戏  udp
        #选牌      
        #人物能力      
        #游戏流程接受     udp
        #投票功能        udp
        # 收发语音       udp
    #结束