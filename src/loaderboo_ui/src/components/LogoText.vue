<script setup>
defineProps({
  msg: {
    type: String,
    required: true,
  },
})
</script>

<template>
  <div class="greetings">
    <h1 class="logo">{{ msg }}</h1>
  </div>
</template>

<style>
h1 {
  font-weight: bold;
  font-size: 3rem;
  position: relative;
  top: -10px;
}

.logo{
  text-decoration: none;
  color: black;
  font-weight: bold;
  transition: 0.4s;
  padding: 3px;
  -webkit-text-stroke: 1px;
  -webkit-text-stroke-color: white;
  
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

header{
  background-color: rgba(255, 255, 255, 0.6);
  border: 0.2rem;
  border-color: rgb(51, 51, 51);
  border-style: solid;
  border-radius: 2em;
}

</style>
