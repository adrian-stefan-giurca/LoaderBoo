<script setup>
import { convertStatus, confirmAnimeEpDownload } from '../../main'

const props = defineProps({
    anime_obj: Object
})

const img_alt = props.anime_obj.name + " image"

function getStatusColor(status){
    if (status == 1){
        return "blue";  // Cambiar por otro azul más claro
    }else if (status == 2){
        return "orange";
    }else if (status == 3){
        return "green";
    }else{
        return "white";
    }
}

</script>

<template>
    <div v-on:click="confirmAnimeEpDownload(props.anime_obj.identifier)" id="result" class="anime-container">
        <img class="anime-image" v-bind:alt="img_alt" v-bind:src="props.anime_obj.image"/>
        <div>
            <p>{{ props.anime_obj.name }}</p>
            <p>{{ props.anime_obj.year }}</p>
            <p id="status_txt" class="info_txt" :style="{ 'color': `${getStatusColor(props.anime_obj.status)}`}">
                {{ convertStatus(props.anime_obj.status) }}
            </p>
            <p id="episodes_txt" class="info_txt">{{ props.anime_obj.episodes }} Episodes</p>
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

.anime-container{
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

#result:hover{
    cursor: pointer;
    background-color: rgb(255, 219, 41);
    border-color: rgb(255, 219, 41);
    color: black;
}

.info_txt{
    font-size: 0.8rem;
}

#episodes_txt{
    align-self:last baseline;
}

</style>