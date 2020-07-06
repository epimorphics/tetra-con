<template>
    <main id="results-block">
        <router-link id="link" to="/">Back</router-link>
        
        <h3 id="header"></h3>
        <section id="results" >
       
        </section>
        
        <section id="card">
            <ul>
                <li id="text" v-for="bay in userSearch" :key="bay.bayId"> 
                    <router-link :to="{ name: 'indivbay', params: {bayId:bay.bayId}}">Get info</router-link> Bay id {{bay.bayId}} on  {{bay.street}} in postcode {{bay.postcode}} </li>
                </ul>
            
            <p id="distance">Distance</p>
        </section>
    </main>
</template>

<script>

export default {
    name: "results",
    data() {
        return {
            inputPostcode: '',
            results: [],
            bayId: this.$route.params.bayId,
            
        }
    },
    computed: {
        bays() {
            return this.$store.state.bays
        },
        userSearch() {
            return this.$store.getters.getInputPostcode
            //acceses the value from the getter
    },
    
    
    }
}
</script>

<style>

</style>