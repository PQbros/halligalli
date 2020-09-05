<template>
  <div id="wrapper">
    <MessageBox :gameMsg=gameMsg />
    <Ring />
    <div id="cards">
      <Card v-for="player in playerNum" :key="player" :cardData=player />
    </div>
    <div id="players">
      <Player
        v-for="player in players"
        :key="player"
        :playerData=player
      />
    </div>
    <ReadyBtn
      @changeready="changeReady"
    />
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
      playerNum: ["1", "2", "3"],
      players: [
        {
          name: "A",
          cardLeft: 10
        },
        {
          name: "B",
          cardLeft: 9
        },
        {
          name: "C",
          cardLeft: 1
        }
      ],
      ready: false
    }
  },
  computed: {
    gameMsg() {
      return this.ready ? "等待房主开始" : "请准备"
    }
  },
  methods: {
    changeReady() {
      this.ready = !this.ready
    }
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
</style>
