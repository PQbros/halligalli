<template>
  <div class="ring">
    <h1>铃</h1>
  </div>
</template>

<script>
export default {
  name: "Ring"
}
</script>

<style scoped>
.ring {
  color: black;
  width: 100px;
  height: 100px;
  border-radius: 50px;
  background-color: rgba(68, 63, 63, 0.384);
  position: absolute;
  top: 30%;
  left: 50%;
  transform: translate(-50%, -50%);
  line-height: 100px;
  text-align: center;
  cursor: pointer;
  -webkit-user-select: none;
}
</style>