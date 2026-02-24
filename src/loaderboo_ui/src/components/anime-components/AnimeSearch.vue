<script setup>
import axios from 'axios';
import AnimeSearchResults from './AnimeSearchResults.vue';

let showAnimeSearch = ref(true);
async function animeSearchRequest(anime_title){
    /**
     * Function in charge of requesting search results to LoaderBoo API and 
     * display them on the screen by creating AnimeSearchResults components
     */
    const url_request = "http://127.0.0.1:8000/anime/search_anime/" + anime_title;
    try {
        const response = await axios.get(url_request);
        console.log(response);
    } catch (error) {
        console.error(error);
    }

    // hide search bar
    showAnimeSearch.value = false;


}

</script>

<template>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <div v-show="showAnimeSearch" class="anime-search-container">
        <div class="menu-text">
            <h2>Enter the title and the season that you want to watch</h2>
            <p>e.g: Frieren Season 2</p>
        </div>
        
        <div class="search-box">
            <input class="search" type="text" id="search-input" placeholder="Search...">
            <p v-on:click="animeSearchRequest('Frieren')" class="search-button"><i class="fa fa-search"></i></p>
        </div>
        
    </div>
</template>

<style>
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