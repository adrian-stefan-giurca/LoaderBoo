<script setup>
const props = defineProps({
    anime_obj: Object
})

const img_alt = props.anime_obj.name + " image"

async function downloadAnime(params) {
    /**
     * Función que se encarga mandar la petición de descargar anime 
     * a la API de LoaderBoo
     */
}

function convertStatus(status){
    if (status == 1){
        return "Upcoming";
    }else if (status == 2){
        return "Ongoing";
    }else if (status == 3){
        return "Completed"
    }else{
        return "Unknown";
    }
}

</script>

<template>
    <div class="result-container">
        <img class="anime-image" v-bind:alt="img_alt" v-bind:src="props.anime_obj.image"/>
        <div class="">
            <p>{{ props.anime_obj.name }}</p>
            <p>{{ props.anime_obj.year }}</p>
            <p>{{ convertStatus(props.anime_obj.status) }}</p>
            <p>Episodes: {{ props.anime_obj.episodes }}</p>
        </div>
        
    </div>
</template>

<style>

p{
    font-size: 1.25rem;
}

.anime-image{
    max-height: 20rem;
    border-radius: 2em; 
    background-color: rgb(50, 50, 50);
    color: black;
}

.result-container{
    transition: all 0.2s;
    background-color: rgb(9, 9, 9);
    border: 0.2rem;
    border-color: rgb(51, 51, 51);
    border-style: solid;
    border-radius: 2em; 
    font-size: 1rem;
    overflow: hidden;
    padding: 1.25rem;
}

.result-container:hover{
    cursor: pointer;
    background-color: rgb(255, 219, 41);
    border-color: rgb(255, 219, 41);
    color: black;
}

</style>