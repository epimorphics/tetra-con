<template>
  <div id="app">
    <h1 id="header">App view Disabled Parking App</h1>
    <nav>
      
      <router-view></router-view>
    </nav>
    
    <!-- <router-view/> will double up as telling it to render the component again-->
   <footer id="footer">Find disabled bays on the go!</footer> 
  </div>
</template>
<script>



export default {
  
  name: 'App',
  components: {
    
  },
  data() {
    return {
      
      
        }

  },
  
  computed: {

    
  },
  mounted () {
    this.$store.dispatch("loadInitialData")
  }
}

</script>

<style>
#app {
  display: grid;
  font-family: sans-serif;
  text-align: left;
  background-color: #F9F9F9;
  padding: 1vw;
  
  
}

#header {
  color: #333333;
  font-weight: 700;
  padding: 1vw;
}

#text {
   color: #1A4C7A;
   list-style-type: none;
   padding: 1vw;
}

#list {
  list-style-type: none;
}


#link {
  text-decoration: none;
  text-align: left;
  padding: 1vw;
}


#search {
    
    grid-column-start: 1;
    grid-column-end: 4;
    grid-row: auto;
    background-color: #FFAD0A;
    box-shadow: 0px 0px 6px 0px lightgray;
    padding: 1vw;
}
#inputbox {
  background-color: lightgray;
  color: #4682AA;
  border-style: solid;
  border-width: medium;
  border: #2E2963;
  border-radius: 4px;
  padding: 8px 20px;
  
}
#results {
  color: #4682AA;
  list-style-type: none;
  background-color: #FFAD0A;
  font-weight: 600;
}

#search-results {
  background-color: #EC8C32;
  margin: 20px 300px;
  border-style: solid;
  border-width: medium;
  border: #2E2963;
  border-radius: 3px;
}

#button {
    display: inline-block;
    background-color: #4682AA;
    color: #333333;
    padding: 8px 20px;
    margin: 5px;
    border: none;
    border-radius: 4px;
    font-weight: 600;
    text-decoration: none;
}
#results-block {
    display: block;
    grid-column: auto;
    grid-row: auto;
    background-color: #F9F9F9;
    box-shadow: 5px 5px lightgray;
    color: #4682AA;
    padding: 20px;
    max-width: 100vw;
}

#card {
    color: #4682AA;
    box-shadow: 0px 4px 6px 0px lightgray;
    color: #4682AA;
    background-color: #FFAD0A;
    margin: 10px;
}

#distance {
    color: #4682AA;
    text-align: right;
}
#footer {
  color: #4682AA;
  font-weight: 700;
  font-style: italic;
  padding: 1vw;
}
</style>
