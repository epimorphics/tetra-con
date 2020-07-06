<template>
  <div class="home">
    
    <search></search>
  </div>
</template>

<script>
// @ is an alias to /src
//import store from '@/store/store.js'
import search from '@/components/search'
export default {
  name: 'Home',
  components: {
    search,
  },
  data() {
    return {
      inputPostcode: ''
    }
  }
}
</script>
<style>

</style>
