<script setup>
const props = defineProps({
    name: String,
    year: Number,
    status: Number,
    image_url: String,
    episodes: Number
})

const img_alt = props.name + " image"

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
        <img class="anime-image" v-bind:alt="img_alt" v-bind:src="props.image_url"/>
        <div class="">
            <p>{{ name }}</p>
            <p>{{ year }}</p>
            <p>{{ convertStatus(props.status) }}</p>
            <p>Episodes: {{ episodes }}</p>
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
}

.result-container{
    transition: all 0.2s;
    background-color: rgb(9, 9, 9);
    border: 0.2rem;
    border-color: rgb(51, 51, 51);
    border-style: solid;
    border-radius: 2em; 
    font-size: 1.25rem;
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