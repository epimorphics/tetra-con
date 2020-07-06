<template>
    <div>
        <h3 id="text" >Where do you want to go?</h3>
    
    <form @submit.prevent="">
      <input id="inputbox" type="text" :v-model="inputPostcode" @input="updateInput" > 
      <!-- call updateInput method -->
      <button id="button"><router-link to="results">Search</router-link></button>
    </form>

    <form @submit.prevent="">
      <input id="inputbox" type="text" :v-model="journeyStart" @input="updateStart">
      <button id="button">Set home postcode</button>
    </form>
    <h3>home postcode is {{userPostcode}}</h3>
    <section>
      <h3 id="text" >Recent searches</h3>
      
      <ul>
        <li id="text"></li>
      </ul>
    </section>
    </div>
</template>

<script>

export default {
    data() {
      return {
        inputPostcode: '',
        journeyStart: '',
        results: []
      }
    },
    computed: {
      bays() {
        return this.$store.state.bays;
      },
      userPostcode() {
        return this.$store.getters.getStartPostcode
      }
    },
    methods: {
      updateInput (e) {
        this.$store.commit('setInputPostcode', e.target.value) //commit the value to setInputPostcode in store
      },
      updateStart (e) {
        this.$store.commit('setStartPostcode', e.target.value)
      },
      
    },
    
    

mounted () {
    this.$store.dispatch("loadInitialData")
    this.$store.dispatch("updateInput")
    this.$store.dispatch("updateStart")
}
}
</script>
<style>

</style>