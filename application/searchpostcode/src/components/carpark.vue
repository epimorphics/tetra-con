<template>
    <div id="carpark">
        <h3>Find carparks</h3>
        <form>
            <label>Select City </label>
            <select name="cities" id="cities" >
                <option value="bristol" >Bristol</option>
                <option value="birmingham">Birmingham</option>
            </select>
        </form>
    </div>
</template>

<script>
export default {
    name: "carpark",
    computed: {
        carparks() {
            return this.$store.state.carparks;
        }
    }
    
}
</script>

<style>
#carpark {
    display: inline;
    grid-column-start: 1;
    grid-row: auto;
    border-style: solid;
    border-color: #ED4F33;
    max-width: 300px;
    padding: 20px;
}
#cities {
    background-color: #ADD2D8;
    color: #2E2963;
}
</style>