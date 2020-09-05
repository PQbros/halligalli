<template>
  <div class="game-msg-box">
    <span>{{  gameMsg }}</span>
  </div>
</template>

<script>
export default {
  name: "MessageBox",
  props: {
    gameMsg: String
  }
}
</script>

<style scoped>
.game-msg-box {
  width: 80%;
  height: 5%;
  margin: 0 auto;
  text-align: center;
  background-color: #ccc;
  position: absolute;
  top: 5vh;
  left: 50%;
  transform: translateX(-50%);
}

.game-msg-box span {
  line-height: 5vh;
  font-size: 18px;
}
</style>