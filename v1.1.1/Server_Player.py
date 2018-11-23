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

    def vote(self,votelist):
        pass

    def 发言():
        pass



    #预言家功能seer验人
    def check_identity(self,player):
        '''
        参数 player 玩家对象 
        功能 验人
        返回 bool 好人 True 坏人 False
        '''
        
        if player.identity == "wolf":
            return False
        return True

    #狼人功能:投票杀人
    def vote_to_kill(self,isalive):
        '''
        参数:isalive 存活列表
        功能:投票杀人
        返回:killedcfd 投票被杀对象 
        '''
        #票杀
        pass

class witch(Player):
    def __init__(self,cfd):
        super().__init__()
        self.identity = 'witch'

    def kill(self,isalive):
        '''
        参数:存活列表
        功能:毒杀
        返回:cfd 毒死的人
        '''
        pass
    def help(self,killedcfd):
        '''
        参数:当局死亡玩家 killedcfd
        功能:救起被杀玩家
        返回:None
        '''
        killedcfd.isalive = True


class hunter(Player):
    def __init__(self,cfd):
        super().__init__()
        self.identity = 'hunter'
    
    def kill_or_not(self):
        '''
        参数:无
        功能:选择是否杀人
        返回:杀 True 不杀 False
        '''
        if self.isalive == False:
            pass


    def kill(self,cfd):
        '''
        参数:猎人要杀的人 cfd
        功能:杀人
        返回:cfd 的生存状态改为False
        '''
        if self.kill_or_not() == True:
            cfd.isalive = False
