<template>
  <div id="app">
    <h1>Welcome</h1>
    <p>Search by postcode</p>
    <form>
      <label>Destination Postcode</label>
      <input id="inputbox" type="text" >
      <!--add submit -->
    </form>
    <section>
      <!--<h3>Parking Bays in {{inputPostcode}}</h3>-->
      
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
  
  //computed properties used to get data from the store
  computed: {
    bays() {
      return this.$store.state.bays; //sets the state
    },
    
  },
  mounted () {
    this.$store.dispatch("loadInitialData")
  }
}

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
</style>