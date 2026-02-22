<script setup>
</script>

<template>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <div class="menu-container">
        <div class="menu-text">
            <h2>Select the content you want to Download</h2>
            <p>You will be redirected to its module</p>
        </div>
        
        <p  class="button">Anime</p>
        <p class="button">YouTube</p>
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