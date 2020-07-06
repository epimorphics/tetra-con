<template>
    <div>
        
        <router-link id="link" to="results">Back</router-link>
        <router-view></router-view>
        
        <section id="card">
            <h3>Result 1</h3>
            <p>Number of spaces</p>
            <p>Address</p>
            <p>Distance</p>
            <button id="button" >Let's Go!</button>
        </section>
    </div>
</template>

<script>
export default {
    
}
</script>

<style>

</style>