<template>
    <div id="payment">
        <h3>Payment</h3>
         <p>Free bays</p>
         
        <p id="payment-results" v-for="space in freeSpaces" :key="space.bayId">{{space.street}}</p>
       <!-- <p v-if="bays.charge">{{bays.street}} has Charge for use</p>
        <p v-else>{{bays.street}}Free parking</p> -->
        
    </div>
</template>

<script>
export default {
    name: "payment",
    
    computed: {
        freeSpaces() {
        return this.$store.getters.freeSpaces;
    }
    
}
}
</script>

<style>
#payment {
    display: inline;
    grid-column-start: 1;
    grid-row: auto;
    border-style: solid;
    border-color: #ED4F33;
    max-width: 300px;
    padding: 20px;
}
</style>