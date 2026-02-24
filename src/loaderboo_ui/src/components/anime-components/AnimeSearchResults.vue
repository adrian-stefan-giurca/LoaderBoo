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
    <div>
        <img v-bind:alt="img_alt" v-bind:src="props.image_url"/>
        <div>
            <p>{{ name }}</p>
            <p>{{ year }}</p>
            <p>{{ convertStatus(props.status) }}</p>
            <p>Episodes: {{ episodes }}</p>
        </div>
        
    </div>
</template>

<style>

</style>