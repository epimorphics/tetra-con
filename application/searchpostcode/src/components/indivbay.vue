<template>
    <div>
        <router-link id="link" to="results">Back</router-link>
        <section id="card">
            <h3>Information for bay</h3>
            <p>home postcode is {{userPostcode}} for the start location</p> 
            <p>Bay id is {{indivResult.bayId}}</p>
            <p>on {{indivResult.street}}</p>
            <p>Number of spaces</p>
            <p>Address</p>
            <p>Distance {{distance}} miles</p>
            
            <button id="button" >Let's Go!</button>
        </section>
    </div>
</template>

<script>
import Geography from '@/Models/geography.js'
//import Start from '@/Models/start.js'
export default {
    name: 'indivbay',
    data() { //return data from params
        return {
            bayId: this.$route.params.bayId, //takes the id from the url
            bays: {}, //what will be returned
            journeyStart: '', //to get start postcode 
            eastings: 360887, 
            northings: 171007
        }
    },
    computed: {
        indivResult() {
            return this.$store.state.bays.find(
                bay => String(bay.bayId) === this.bayId
            )
        },
        //returns the home postcode entered on the search page
        userPostcode() {
        return this.$store.getters.getStartPostcode
        },
        distance () {
            return Geography.distance(this.indivResult, this.startObj[0]) //obj1 and obj2 the two sets of eastings and nortings
        },
        //just to use the Start class and see if it works - it doesn't
        startLocation() {
            return this.$store.state.start
        },
        startObj() {
            return this.$store.state.start
        }
      
        }
}


    
    
</script>

<style>

</style>