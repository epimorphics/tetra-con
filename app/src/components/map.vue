<template>
    <div>
        <router-link to="home">Home</router-link>
        <h3>Map View</h3>
    </div>
</template>

<script>
export default {
    
}
</script>
<style>
#map {
    display: block;
    grid-column-start: 2;
    grid-column-end: 4;
    grid-row: auto;
    border-style: solid;
    border-color: #ED4F33;
    max-width: 100vw;
    padding: 20px;
}
</style>