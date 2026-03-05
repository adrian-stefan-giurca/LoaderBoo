<script setup>
import AnimeCover from './AnimeCover.vue';
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router'

const search_response = ref([]);
const route = useRoute();

async function animeSearchRequest(anime_title){
    /**
     * Function in charge of requesting search results to LoaderBoo API and 
     * display them on the screen by creating AnimeSearchResults components
     */
    const url_request = "http://127.0.0.1:8000/anime/search_anime/" + anime_title;
    try {
        const response = await axios.get(url_request);
        console.log(response);
        search_response.value = response.data
    } catch (error) {
        console.error(error);
        return -1;
    }

}

onMounted(() => {
    animeSearchRequest(route.params.search_term)
})

console.log(search_response.value)

</script>

<template>
    <p class="result-instructions">
        Select the anime series to download 
    </p>

    <div class="search-results-container">

        <AnimeCover v-for="res in search_response" :anime_obj="res" />

    </div>
</template>

<style>
.result-instructions{
    padding-bottom: 2rem;
}

.search-results-container{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    row-gap: 3rem;
    column-gap: 10rem;
}

</style>