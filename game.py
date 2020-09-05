from player import Player
import random
import json


class Game:
    def __init__(self, player_num, player_list):
        self.playerList = player_list  # 每个人初始的手牌
        self.playerNum = player_num
        self.deskCard = []  # 桌面上的牌
        self.players = []  # 所有玩家
        self.fruitNum = {'b': 0, 'l': 0, 'a': 0, 'p': 0}  # 桌上的水果的总数
        self.ring = 0  # 0的时候按铃就惩罚 1的时候按就奖励
        self.status = 0  # 1表示游戏开始 0表示游戏未开始

    def start(self):
        # playerNum = int(input("Enter the number of players:"))
        # self.playerNum = playerNum
        for i in range(self.playerNum):
            a = Player()
            self.players.append(a)
        self.dealCards(self.playerNum)  # 发牌
        for j in range(self.playerNum):
            self.players[j].inCards = self.playerList[j]
        self.status = 1

    def dealCards(self, playerNum):
        with open('./cards.json', 'r') as load_f:
            init_card = json.load(load_f)
        random.shuffle(init_card)
        unitCard = 56 // self.playerNum
        while playerNum > 0:
            self.playerList.append([])
            playerNum -= 1
        for i in range(0, self.playerNum):
            self.playerList[i] = [r for r in init_card[i*unitCard:(i+1)*unitCard]]
        
        return self.playerList

    def popCard(self, player): # 打牌
        newCard = player.inCards.pop()
        player.outCards.insert(0,newCard)
        self.deskCard.insert(0, newCard)
        self.fruitNum[newCard.get('fruit')] += newCard.get('number')

    def checkRing(self): # 检查按铃是否正确
        for value in self.fruitNum.values():
            if value >= 5:
                self.ring = 1

    def reward(self, player):# 奖励
        for card in self.deskCard:
            player.inCards.append(card)
        random.shuffle(player.inCards)
        self.deskCard = []
        self.fruitNum = {'b':0, 'l':0, 'a':0, 'p':0} # 桌上数据全部重置
        for aPlayer in self.players:
            aPlayer.outCards = []
        self.ring = 0
    
    def punish(self,player): # 惩罚
        if len(player.inCards) >= self.playerNum-1: # 手牌够发给其他玩家
            for i in range(self.playerNum):
                if i == self.players.index(player):
                    continue
                else:
                    card = player.inCards.pop()  #一人发一张
                    self.players[i].inCards.append(card)
        else:
            if len(player.inCards) > 0: # 不够发但还有
                for i in range(len(player.inCards)):
                    card = player.inCards.pop()
                    self.deskCard.append(card)  #全部反面向上 丢到桌子上（不改变桌上水果的数量）
            else:
                player.outCards = [] # 没有手牌了还乱按铃 直接GG
                self.checkSituation(player)

    def checkSituation(self, player):
        if player is None: # GG的孩子
            return None
        if len(player.inCards) == 0 and len(player.outCards) == 0:
            self.players[self.players.index(player)] = None 
            # 继续游戏
        temp_list = [] 
        for i in self.players:
            if i is not None:
                temp_list.append(i)
        if len(temp_list) == 2: 
            if len(temp_list[0].inCards) > len(temp_list[1].inCards):
                self.status = "{} wins!!".format(temp_list[0].name)
                # 玩家1赢了！！
            elif len(temp_list[0].inCards) < len(temp_list[1].inCards):
                self.status = "{} wins!!".format(temp_list[1].name)
                # 2 !!!
            #else:
                # 继续游戏

def main():
    q = Game()
    q.start()
    while q.status == 1:
        for i in range(len(q.players)):
            if q.players[i] is None:
                continue
            print(i) # 玩家序号
            print(q.players[i].inCards) # 手牌
            hello = input("Enter 'd' to pop a card:")
            if q.players[i].inCards != []:  # 确保没有手牌了但打出去的牌还没被收走的玩家还有按铃的机会
                q.popCard(q.players[i])
            print(q.players[i].inCards)
            print(q.players[i].outCards)
            print(q.fruitNum)
            hi = input("Enter number to ring:") # 为了测试方便，输入玩家序号以表示该玩家按了铃
            if hi != 'r': # 按r表示没人按铃
                q.checkRing()
                if q.ring == 0:
                    q.punish(q.players[int(hi)])
                else:
                    q.reward(q.players[int(hi)])
            print(q.deskCard)
            for m in range(len(q.players)):
                q.checkSituation(q.players[m])
                if q.status != 1:
                    break
            print("Status: ", q.status)
            if q.status != 1:
                break


if __name__ == "__main__":
    main()