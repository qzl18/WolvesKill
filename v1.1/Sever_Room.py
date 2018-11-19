from threading import Thread
# import random
import os
'''
玩家创建Room,传入player对象
Room的属性:
玩家人数
房间可容纳人数
玩家列表([player对象])
随机生成的房间号
##########
身份列表
狼人列表
村民列表
神列表
''' 
class Room():
    def __init__(self,player):
        self.player = player
        
    #创建房间,player是用户对象
    def create(self,size=2):
        self.count = 0
        self.size = size
        self.player_list= [self.player]
        # self.room_number = random.randint(1,9999)
        self.room_number = os.getpid()#pid号就是房间号
        # self.wolf_count = 3
        # self.god_count = 3
        # self.villagerr_count = 3
        self.identity = ["seer","witch",'hunter','villager',"villager","villager",'wolf','wolf','wolf']
        self.wolf_list = []
        self.villager_list = []
        self.god_list = []
        return True


    def join(self,player):
        print("join %d "%int(os.getpid()))
        self.room_number = os.getpid()
        self.player_list.append(player)
        return True
        pass




    def start_game(self):
        if self.count != self.size-1:
            self.count += 1
            print(self.count)
        else:
            self.game()

    def game(self):
        #---------游戏所有人都准备好了,真正开始游戏--------------
        msg = b"OK"
        for i in self.player_list:
            i.s.sendto(msg,i.addr)
        pass




    



    def show(self):
        print("############ROOM################")
        print("self.player=",self.player)
        print("self.count=",self.count)         
        print("self.size= ",self.size)
        print("self.player_list=",self.player_list)
        print("self.room_number",self.room_number)
        print("self.wolf_list= ",self.wolf_list)
        print("self.villager_list",self.villager_list)
        print("self.god_list",self.god_list)
# ####################################################################
#     #加入游戏房间,刚进入编号为None,添加到字典
#     def join(self):
#         '''
#         加入#加入游戏房间,刚进入编号为None,添加到字典
#         type(c)      套接字对象
#         return: bool 能否成功加入房间
#         '''
#         if self.count <= 9:
#             self.playerfd_num[cfd]= None
#             self.count += 1
#             return True
#         else:
#             return False
        

#     #用户选择编号(1~9)
#     def choice_num(self,cfd,num):  
#         self.playerfd_num[cfd] = num

#     def quit(self,cfd)
#         if cfd in self.playerfd_num:
#             self.playerfd_num.pop(cfd)
#             #然后断开链接
#             断开链接

#     #掉线重连
#     def funcname(self, parameter_list):
#         pass
#     #点击开始游戏
#     def click_start(self):
#         #self.admin 点击开始游戏
#         pass
#     def is_over(self):
#         #狼人列表中无存活者
#         for i in self.wolf_list:
#             if i.isalive == True:
#                 count += 1
#         if count == 0:
#             print("神民胜利")
#         #神列表中无存活者
#         for i in self.god_list:
#             if i.isalive == True:
#                 count += 1
#         if count == 0:
#             print("狼人胜利")
#         #村民列表中无存活者
#         for i in self.villager_list:
#             if i.isalive == True:
#                 count += 1
#         if count == 0:
#             print("狼人胜利")
        

#     #游戏开始
#     def play_game(self):
#         #随机身份,播放语音
#         pass
#         playerfd_identity = {}
#         L = random.shuffle(self.identity)
#         for cfd in self.playerfd_num:
#             playerfd_identity[cfd] = (playerfd_num[cfd],L[i-1])
#             #playerfd_identity = {cfd:(num,identity)}
#         #创建阵营列表
#         for cfd in self.playerfd_identity:
#             if playerfd_identity[cfd][1] == "wolf":
#                 self.wolf_list.append(cfd)#
#             elif playerfd_identity[cfd][1] == "villager":
#                 self.villager_list.append(cfd)
#             else:
#                 self.god_list.append(cfd)
#         #创建玩家存活字典
#         for cfd in playerfd_identity:
#             #self.alive_dict = {cfd:True}
#             self.alive_dict[cfd] = True

#         #传送身份信息给客户端
#         pass
#         #开始游戏
#         self.click_start()

#         while True:
#             #天黑阶段
#             #天黑请闭眼,播放语音
#             pass
#             #狼人请睁眼,狼人选择猎杀对象并投票
#             #wolf_part()
#             pass
#             #女巫请睁眼,选择毒还是解药
#             # witch_part()
#             pass
#             #预言家请睁眼,选择验人
#             # seer_part()
#             pass
#             #猎人请睁眼,查看自身状态,选择是否开枪
#             # hunter_part()
#             pass

#             #天亮阶段:
#             '''
#             #竞选警长()
#             #if self.police == None:
#                 #vote_police()
#                 pass
#                 #self.police = vote_police()
#             '''
#             #宣布死亡,更新存活字典
#             pass
#             #投票驱逐阶段,警长选择发言顺序,更新存活字典
#             #player = vote()
#             # self.alive_dict[player] =False

#             #判断胜利条件
#             self.is_over()

                    
                        
if __name__ == "__main__":
    
    r = Room(cfd)