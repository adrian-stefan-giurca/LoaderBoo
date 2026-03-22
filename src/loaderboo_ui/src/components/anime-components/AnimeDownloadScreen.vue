<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from "vue-router"
import { inputAnimeSearch } from '../../main'
import axios from 'axios';

const route = useRoute();
const downlaod_status = ref(null);

async function downloadAnime(anime_title, anime_id, episode) {
    /**
     * Function in charge of sending a download_anime request to 
     * LoaderBoo API, it will send the received parameters in the 
     * request as they are needed in the backend to download 
     * the episode
     */
    const url_request = "http://127.0.0.1:8000/anime/download_anime/" + anime_title + "/" + anime_id + "/" + episode;
    try {
        const response = await axios.post(url_request);
        downlaod_status.value = response
    } catch (error) {
        console.error(error);
        return -1;
    }
}

onMounted(() => {
    downloadAnime(route.params.anime_title, route.params.anime_id, route.params.ep)
})

// TODO: posible solución para pantalla de progreso de la descarga ->
// Frontend haciendo polling continuamente al backend sobre su progreso

</script>

<template>
    <div class="download-page">
        <p v-if="downlaod_status == null">
            Downloading episode ...
        </p>

        <div id="download-complete-options" v-else>
            <p>
                Download complete!
            </p>

            <p class="button" v-on:click="inputAnimeSearch()">
                Download more anime
            </p>
        </div>
    </div>
    
</template>

<style>

#download-complete-options{
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

</style>