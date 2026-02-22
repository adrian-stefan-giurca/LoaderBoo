<script setup>
import LogoText from './components/LogoText.vue'
import WelcomeMenu from './components/WelcomeMenu.vue';
import AnimeSearch from './components/anime-components/AnimeSearch.vue';
</script>

<template>
  <header class="logo_header">
    <div class="wrapper">
      <LogoText msg="LoaderBoo" />
    </div>

    <img alt="Vue logo" class="logo_img" src="./assets/loaderboo_logo.webp" width="125" height="125" />
  </header>

  <main>
    <AnimeSearch/>
  </main>

  <!-- <main>
    <WelcomeMenu/>
  </main> -->
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo_img {
  display: block;
  margin: 0 0 0 2rem;
}

.logo_header{
  max-width: fit-content;
  display: flex;
  place-items: center;
  overflow: hidden;
  padding: 0 0 0 2rem;
}


</style>
