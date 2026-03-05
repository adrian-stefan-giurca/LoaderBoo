<script setup>
import { ref } from 'vue';
import { useRouter } from "vue-router"

const anime_search_term = ref();
const route = useRouter()

function startAnimeSearch(anime_title){
    route.push({
        path: `/anime-search/${anime_title}` 
    })
}

</script>

<template>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <div class="anime-search-container">
        <div class="menu-text">
            <h2>Enter the title and the season you want to watch</h2>
            <p>e.g: Frieren Season 2</p>
        </div>

        <div class="search-box">
            <input v-model="anime_search_term" class="search" type="text" id="search-input" placeholder="Search...">
            <p v-on:click="startAnimeSearch(anime_search_term)" class="search-button">
                <i class="fa fa-search"></i>
            </p>
        </div>
        
    </div>

</template>

<style>

.search-results-container{
    display: grid;
    /* align-items: center; */
    /* text-align: center; */
    grid-gap: 1rem;
    place-items: center;
}

.anime-search-container{
    display: grid;
    align-items: center;
    text-align: center;
    grid-gap: 1rem;
    place-items: center;
}

.search-box{
    display: flex;
    align-items: center;
    text-align: center;
    grid-gap: 1rem;
    place-items: center;
}

.search-button, .search{
    transition: all 0.2s;
    background-color: rgb(9, 9, 9);
    border: 0.2rem;
    border-color: rgb(51, 51, 51);
    border-style: solid;
    border-radius: 2em; 
    font-size: 1.25rem;
}

.search-button{
    padding: 0 0.75rem;
}

.search{
    padding: 0 30rem 0 0.75rem;
    color: white;
}

.search-button:hover{
    cursor: pointer;
    background-color: rgb(255, 219, 41);
    border-color: rgb(255, 219, 41);
    color: black;
}
</style>