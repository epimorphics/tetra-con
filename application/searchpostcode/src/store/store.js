import Vue from 'vue'
import Vuex from 'vuex'
import mockData from './mock2.json'
import 'core-js'
Vue.use(Vuex);

export const store = new Vuex.Store ({
    state: {
      //complete initial starting 
          // myjson: data,
          bays: [], //initialise as an empty array
          carparks: [],
          count: 0
        
    },
    mutations: {
      increment (state) {
        state.count++
      },
      setBays: (state, newBays) => {
        state.bays = newBays
      },
      setCarparks: (state, newCarpark) => {
        state.carparks = newCarpark
      },
    },
    getters: {
      freeSpaces: state => {
        return state.bays.filter(bays => !bays.charge); 
      }
    },
    actions: {
      loadInitialData: context => {
        // could do here: call the server to get the bays data
        // Axios
        //   .get('/api/bays')
        //   .then(response => {
        //     const baysData = JSON.parse(response.body)
        //     context.commit('setBays', baysData)    
        //   })

        // but instead we use the fixed data we import above
        context.commit('setBays', mockData.bays)
        context.commit('setCarparks', mockData.carparks)
      }
    }
});
store.commit('increment');
//console.log(store.state.count)
console.log(store.getters.freeSpaces)
