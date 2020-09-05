from player import Player
import random
import json

class Game:
    def __init__(self):
        self.playerList = []
        self.playerNum = 0

    def dealCards(self):
        with open('./cards.json', 'r')  as load_f:
            init_card = json.load(load_f)
        playerNum = int(input())
        self.playerNum = playerNum
        random.shuffle(init_card)
        unitCard = 56 // self.playerNum
        while playerNum > 0 :
            self.playerList.append([])
            playerNum -= 1
        for i in range(0, self.playerNum):
            self.playerList[i] = [r for r in init_card[i*unitCard:(i+1)*unitCard]]
        
        return self.playerNum