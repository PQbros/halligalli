<template>
  <div class="player">
    <div class="name">{{  playerData.name  }}</div>
    <div>剩余牌数</div>
    <div class="cardLeft">{{  playerData.cardLeft  }}</div>
  </div>
</template>

<script>
export default {
  name: "Player",
  props: {
    playerData: Object
  }
}
</script>

<style>
.player {
  width: 18%;
  height: 90%;
  border: 1px dashed #000000;
  border-radius: 10%;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
}

.player div{
  height: 30%;
  line-height: 150%;
}
</style>