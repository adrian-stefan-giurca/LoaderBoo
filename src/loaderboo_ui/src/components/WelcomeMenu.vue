<script setup>
import AnimeSearch from './anime-components/AnimeSearch.vue';
import { ref } from 'vue';

let showAnimeSearchMenu = ref(false);
let showWelcomeMenu = ref(!showAnimeSearchMenu.value);

function toggleAnimeSearchMenu(){
    if (showAnimeSearchMenu.value === true){
        showAnimeSearchMenu.value = false
    }else{
        showAnimeSearchMenu.value = true
    }
    showWelcomeMenu.value = !showAnimeSearchMenu.value;
}

</script>


<template>
    <div v-show="showWelcomeMenu" class="menu-container">
        <div class="menu-text">
            <h2>Select the content you want to Download</h2>
            <p>You will be redirected to its module</p>
        </div>
        
        <p v-on:click="toggleAnimeSearchMenu()" class="button anime-button">Anime</p>
        <p class="button">YouTube</p>
    </div>

    <div v-show="showAnimeSearchMenu" class="anime-search">
        <AnimeSearch/>
    </div>
</template>

<style>
.menu-container{
    display: grid;
    align-items: center;
    text-align: center;
    grid-gap: 1rem;
    place-items: center;
}

.button{
    transition: all 0.2s;
    background-color: rgb(9, 9, 9);
    border: 0.2rem;
    border-color: rgb(51, 51, 51);
    border-style: solid;
    border-radius: 2em;
    font-size: 1.25rem;
    width: 15rem;
}

.button:hover{
    cursor: pointer;
    background-color: rgb(255, 219, 41);
    border-color: rgb(255, 219, 41);
    color: black;
}

</style>