<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRoute } from "vue-router"
import { convertStatus, inputAnimeSearch, startAnimeDownload } from '../../main'
import axios from 'axios';


const route = useRoute();
const anime = ref([]);
const img_alt = ref();
const episode_to_download = ref();


onMounted(() => {
    getAnimeInfoRequest(route.params.anime_id)
    img_alt.value = anime.name + " image"
    
})

async function getAnimeInfoRequest(anime_id){
    /**
     * Function in charge of requesting search results to LoaderBoo API and 
     * display them on the screen by creating AnimeSearchResults components
     */
    const url_request = "http://127.0.0.1:8000/anime/get_anime_info/" + anime_id;
    try {
        const response = await axios.get(url_request);
        console.log(response);
        anime.value = response.data
    } catch (error) {
        console.error(error);
        return -1;
    }
}

watch(episode_to_download, (newValue) => {
    // Forzar máximo del input ep-input al escribir con 
    // teclado, el máximo es anime.value.episodes
    episode_to_download.value = newValue > anime.value.episodes ? anime.value.episodes : newValue

})

</script>

<template>
    <div class="download-page">
        <p>
            Check the following info about the anime episode that will be downloaded: 
        </p>

        <div v-if="anime" id="anime-to-download" class="anime-container">
            <img class="anime-image" v-bind:alt="img_alt" v-bind:src="anime.image"/>
            <div>
                <p>{{ anime.name }}</p>
                <p>{{ anime.year }}</p>
                <p>{{ convertStatus(anime.status) }}</p>
                <p>Episodes: {{ anime.episodes }}</p>
            </div>    
        </div>

        <div v-else>
            <p> Loading... </p>
        </div>

        <p>
            Select the episode to download: 
        </p>

        <input id="ep-input" class="search" v-if="anime" type="number" v-model.number="episode_to_download" 
            min="0" v-bind:max="anime.episodes" />


        <div id="download-options">
            <p class="button" v-if="anime" 
            v-on:click="startAnimeDownload(anime.name, route.params.anime_id, episode_to_download)">
                Download
            </p>

            <p class="button" v-on:click="inputAnimeSearch()">
                Go back
            </p>
        </div>
        
    </div>
    
</template>

<style>

.download-page{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2rem;
}

#anime-to-download{
    display: flex;
    flex-direction: row;
    gap: 1rem;
}


#download-options{
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 1rem;
}

#ep-input{
    padding: 0 1rem;
}

</style>