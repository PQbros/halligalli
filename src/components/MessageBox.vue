<template>
  <div class="game-msg-box">
    <span>{{  gameMsg  }}</span>
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
  width: 100%;
  height: 8%;
  margin: 0 auto;
  text-align: center;
  background-color: #ccc;
  position: absolute;
  top: 10%;
  left: 50%;
  transform: translateX(-50%);
}

.game-msg-box span {
  line-height: 5vh;
  font-size: 18px;
}
</style>