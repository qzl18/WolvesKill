import random as R




class Game():
    def __init__(self,room,player_list):
        self.room = room
        self.player_list = player_list
        # 分配号码
        i = 1
        for p in self.player_list:
            p.number = i
            i+=1
        self.identity = ["seer","witch",'hunter','villager',"villager","villager",'wolf','wolf','wolf']
        self.wolf_list = []
        self.villager_list = []
        self.god_list = []
        self.isalive = player_list

    def start(self):
        # 分配身份
        for i in range(9):
            self.player_list[i].identity = R.shuffle(self.identity)[i]
            if self.player_list[i].identity =="villager":
                self.villager_list.append(self.player_list[i])
            elif self.player_list[i].identity =="wolf":
                self.wolf_list.append(self.player_list[i])
            else:
                self.god_list.append(self.player_list[i])
            #----->给每个人发送身份信息
        #游戏流程
        while True:
            #天黑阶段
            #天黑请闭眼,播放语音
            pass
            #狼人请睁眼,狼人选择猎杀对象并投票
            #wolf_part()
            
            pass
            #女巫请睁眼,选择毒还是解药
            # witch_part()
            pass
            #预言家请睁眼,选择验人
            # seer_part()
            pass
            #猎人请睁眼,查看自身状态,选择是否开枪
            # hunter_part()
            pass

            #天亮阶段:
            '''
            #竞选警长()
            #if self.police == None:
                #vote_police()
                pass
                #self.police = vote_police()
            '''
            #宣布死亡,更新存活字典
            pass
            #投票驱逐阶段,警长选择发言顺序,更新存活字典
            #player = vote()
            # self.alive_dict[player] =False

            #判断胜利条件
            self.is_over()


    def is_over(self):
        #狼人列表中无存活者
        count = 0
        for i in self.wolf_list:
            if i.alive == True:
                count += 1
        if count == 0:
            return ("神民胜利")
        #神列表中无存活者
        count = 0
        for i in self.god_list:
            if i.alive == True:
                count += 1
        if count == 0:
            return("狼人胜利")
        #村民列表中无存活者
        count = 0
        for i in self.villager_list:
            if i.alive == True:
                count += 1
        if count == 0:
            return("狼人胜利")
        



            
            
