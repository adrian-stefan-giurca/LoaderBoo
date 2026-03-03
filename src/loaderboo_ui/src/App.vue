<script setup>
import { RouterView } from 'vue-router';

</script>

<template>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <header class="logo_header">
    <h1 class="logo">LoaderBoo</h1>

    <img alt="LoaderBoo logo" class="logo_img" src="./assets/loaderboo_logo.webp" width="125" height="125" />
  </header>

  <main>
    <RouterView />
  </main>

</template>

<style scoped>


.logo_header{
  display: flex;
  align-items: center;
}

header{
  background-color: rgba(255, 255, 255, 0.6);
  border: 0.2rem;
  border-color: rgb(51, 51, 51);
  border-style: solid;
  border-radius: 2em;
  line-height: 1.5;
}


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

.logo_img {
  display: block;
  margin: 0 0 0 2rem;
}

.logo_header{
  /* max-width: fit-content; */
  display: flex;
  place-items: center;
  /* overflow: hidden; */
  padding: 0 0 0 2rem;
  text-align: center;
}


</style>
