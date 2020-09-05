<template>
  <div class="card">
    <h1>{{  cardData  }} </h1>
  </div>
</template>

<script>
export default {
  name: "Card",
  props: {
    cardData: String
  }
}
</script>

<style>
.card {
  width: 18%;
  height: 100%;
  border: 1px dashed #000;
  border-radius: 5%;
}
</style>