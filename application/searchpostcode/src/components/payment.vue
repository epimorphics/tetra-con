<template>
    <div id="payment">
        <h3>Payment</h3>
        <!-- <p>See which bays are free</p>
        <p v-for="bay in bays" :key="bay.bayId"></p>
        <p v-if="bays.charge">{{bays.street}} has Charge for use</p>
        <p v-else>{{bays.street}}Free parking</p> -->
        
    </div>
</template>

<script>
export default {
    name: "payment",
    computed: {
        payments() {
        return this.$store.state.bays
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