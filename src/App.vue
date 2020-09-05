<template>
  <div id="app">
    <div id="wrapper">
      <h1 id="title">德国心脏病</h1>
      <div>
        <MessageBox :gameMsg=gameMsg />
        <div class="start-btn" v-show="isOwner && playerNum > 1" @click="start">开始</div>
      </div>
      <Ring />
      <div id="cards">
        <Card v-for="(card, index) in inCards" :key="index" :cardData=card />
      </div>
      <div id="players">
        <Player
          v-for="(player, index) in players"
          :key="index"
          :playerData=player
        />
      </div>
      <ReadyBtn
        @changeready="changeReady"
      />
    </div>
    <div id="login"
      v-show="showWindow"
    >
      <h3>输入你的用户名</h3>
      <input type="text" v-model="username">
      <div class="login-btn" @click="login">登录</div>
    </div>
  </div>
</template>

<script>
import MessageBox from './components/MessageBox'
import Ring from './components/Ring'
import Card from './components/Card'
import Player from './components/Player'
import ReadyBtn from './components/ReadyBtn'

export default {
  name: 'App',
  data: () => {
    return {
      playerNum: 0,
      inCards: [],
      players: [],
      ready: false,
      isLogin: false,
      showWindow: false,
      isOwner: false,
      username: ""
    }
  },
  computed: {
    gameMsg() {
      if (this.ready) {
        if (this.isOwner && this.playerNum > 1) {
          return "点击开始游戏"
        } else if (this.isOwner) {
          return "等待玩家"
        } else {
          return "等待房主开始"
        }
      } else {
        return "请准备"
      }
    }
  },
  methods: {
    changeReady() {
      if (!this.ready) {
        this.showWindow = true
      }
      if (this.ready) {
        this.$socket.emit('logout', {
          username: this.username
        })
        this.updatePlayers()
      }
      this.ready = !this.ready
    },
    login() {
      if (this.username) {
        this.$socket.emit('login', {
          username: this.username
        })
        this.showWindow = false
        this.isLogin = true
        this.updatePlayers()
      }
    },
    updatePlayers() {
      this.sockets.subscribe('playerList', (data) => {
        console.log(data)
        this.playerNum = data.length
        this.players = []
        data.forEach(element => {
          this.players.push({
            name: element
          })
        });
        if (data[0] === this.username) {
          this.isOwner = true
        }
      })
    },
    start() {
      this.$socket.emit('start')
      console.log(this.playerNum);
    }
  },
  mounted() {
    this.$socket.emit('connection');
    this.updatePlayers()
  },
  components: {
    MessageBox,
    Ring,
    Card,
    Player,
    ReadyBtn
  }
}
</script>

<style>
#wrapper {
  width: 100%;
  height: 100%;
  position: relative;
}

#title {
  position: absolute;
  top: 2%;
  left: 50%;
  transform: translateX(-50%);
  z-index: 10;
}

#cards {
  width: 100%;
  height: 18%;
  position: absolute;
  top: 60%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  justify-content: space-evenly;
}

#players {
  width: 100%;
  height: 12%;
  background-color: #ddd;
  position: absolute;
  top: 80%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  align-items: center;
  justify-content: space-evenly;
}

#login {
  width: 50%;
  height: 10%;
  background-color: #fff;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  z-index: 20;
}

#login input {
  position: relative;
  top: 20%;
  margin: 0 auto;
}

.login-btn {
  width: 60px;
  border: 1px solid black;
  position: relative;
  margin: 0 auto;
  top: 5%;
}

.start-btn {
  position: absolute;
  width: 20%;
  font-size: 20px;
  color: white;
  background-color: red;
  border: 1px solid black;
  left: 50%;
  top: 42%;
  transform: translate(-50%, -50%);
}
</style>
