from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from game import Game

playerList = []
playerNums = 0

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('connection')
def connection():
    print('A user connected')


@socketio.on('login')
def login(data):
    print(data['username'] + " is login")
    playerList.append(data['username'])
    print(playerList)
    socketio.emit('playerList', playerList)


@socketio.on("logout")
def logout(data):
    playerList.remove(data['username'])
    print(playerList)
    socketio.emit('playerList', playerList)


@socketio.on('start')
def start():
    playerNums = len(playerList)
    game = Game(playerNums, playerList)
    game.start()
    while game.status == 1:
        for i in range(len(game.players)):
            if game.players[i] is None:
                continue
            print(i)  # 玩家序号
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
    socketio.run(app)
