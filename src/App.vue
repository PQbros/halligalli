<template>
  <div id="app">
    <div id="wrapper">
      <h1 id="title">德国心脏病</h1>
      <MessageBox :gameMsg=gameMsg />
      <Ring />
      <div id="cards">
        <Card v-for="(card, index) in playerNum" :key="index" :cardData=card />
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
      players: [],
      ready: false,
      isLogin: false,
      showWindow: false,
      username: ""
    }
  },
  computed: {
    gameMsg() {
      return this.ready ? "等待房主开始" : "请准备"
    }
  },
  methods: {
    changeReady() {
      if (!this.ready) {
        this.showWindow = true
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
      }
    }
  },
  mounted() {
    this.$socket.emit('connection');
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
</style>
