import Vue from 'vue'
import Vuex from 'vuex'
import mockData from './mock2.json'
import 'core-js'
Vue.use(Vuex);

export const store = new Vuex.Store ({
    state: {
          bays: [],
          carparks: [],
          
        
    },
    mutations: {
      setBays: (state, newBays) => {
        state.bays = newBays
      },
      setCarparks: (state, newCarpark) => {
        state.carparks = newCarpark
      },
      updatePostcode (state, postcode) {
        state.obj.postcode = postcode
      }
    },
    getters: {
      freeSpaces: state => {
        return state.bays.filter(bays => !bays.charge); 
      },
      
    },
    actions: {
      loadInitialData: context => {
        context.commit('setBays', mockData.bays)
        context.commit('setCarparks', mockData.carparks)
      }
    }
});
//store.commit('increment');

