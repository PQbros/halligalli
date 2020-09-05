<template>
  <div
    class="ready-btn"
    @click="ready"
  >{{  isReady ? "取消准备" : "准备"  }}</div>
</template>

<script>
export default {
  name: "ReadyBtn",
  data: () => {
    return {
      isReady: false
    }
  },
  methods: {
    ready() {
      this.isReady = !this.isReady
      this.$emit('changeready')
    }
  }
}
</script>

<style>
.ready-btn {
  width: 40%;
  height: 5%;
  background-color: red;
  position: absolute;
  top: 93%;
  left: 50%;
  transform: translate(-50%, -50%);
  border-radius: 10px;
  color: white;
  line-height: 250%;
  cursor: pointer;
  background-color: red;
  user-select: none;
}
</style>