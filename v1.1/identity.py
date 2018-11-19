from room import *
class Human():
    def __init__(self,cfd):
        self.socket = cfd
        self.number = None
        self.identity = None
        self.isalive = True
        self.ispolice = False

    def vote(self,votelist):
        pass

    def 发言():
        pass
    def create_room(self):
        self.room = Room()

class villager(Human):
    def __init__(self,cfd):
        super().__init__()
        self.identity = 'villager'

class seer(Human):
    def __init__(self,cfd):
        super().__init__()
        self.identity = 'seer'
    #验人
    def check_identity(self,cfd):
        '''
        参数 cfd 要验的对象 
        功能 验人
        返回 bool 好人 True 坏人 False
        '''
        if cfd.identity == "wolf":
            return False
        return True

class wolf(Human):
    def __init__(self,cfd):
        super().__init__()
        self.identity = 'wolf'
    
    def vote_to_kill(self,isalive):
        '''
        参数:isalive 存活列表
        功能:投票杀人
        返回:killedcfd 投票被杀对象 
        '''
        #票杀
        pass

class witch(Human):
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


class hunter(Human):
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



        


