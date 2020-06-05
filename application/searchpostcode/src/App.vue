<template>
  <div id="app">
    <h1>Welcome</h1>
    <p>Search by postcode</p>
    <form>
      <label>Destination Postcode</label>
      <input id="inputbox" type="text" v-model="inputPostcode" >
      <button @submit.prevent="onSubmit" >Search</button>
      
    </form>
    <section>
      <h3>Parking Bays in</h3>
      
        <p id="results" v-for="bay in bays" :key="bay.street">Street: {{bay.street}} Number of spaces:  {{bay.numSpaces}}</p>
        
        
    </section>
    <carpark ></carpark>
    <payment ></payment>
    
  </div>
</template>

<script>
import carpark from './components/carpark'
import payment from './components/payment'


export default {
  
  name: 'App',
  components: {
    carpark,
    payment
  },
  data() {
    return {
      inputPostcode: null
      
    }

  },
  computed: {
    bays() {
      return this.$store.state.bays;
    },
    comparePostcode() {
      input = this.$data.inputPostcode.match(/BS4/g)
      matched = this.$store.state.bays.postcode.filter(input)
      return matched
      //string matching
      
    }
  },
  mounted () {
    this.$store.dispatch("loadInitialData")
  }
}
// //make a function to do the regex
// function matchInput(item) {
//     return item.match(/BS4/g) //global flag to find all
// }
// let postcodes = ["BS32", "BS33", "BS4", "BS16", "BS40"].filter(matchInput)
// console.log("ran through filtered", postcodes)

</script>

<style>
#app {
  display: grid;
  font-family: Verdana, Geneva, Tahoma, sans-serif;
  text-align: center;
  background-color: #F5B12E;
  color: #2E2963;
  
}
#inputbox {
  background-color: #ADD2D8;
  border-style: solid;
  border-width: medium;
  border: #2E2963;
  border-radius: 3px;
}
#results {
  background-color: #ED4F33;
  margin: 20px 300px;
}

#payment-results {
  background-color: #ED4F33;
}
</style>