import Vue from 'vue'
import Vuex from 'vuex'
import mockData from './mock2.json'
import Bay from '@/Models/bay.js'
import Start from '@/Models/start.js'

Vue.use(Vuex);

export const store = new Vuex.Store ({
    state: {
          bays: [],
          inputPostcode: '',
          start: [],
          journeyStart: '',
          carparks: [],
          
        
    },
    //mutations change the state
    mutations: {
      setBays: (state, newBays) => {
        state.bays = newBays.map(bay => new Bay(bay))
      },
      //maps the start object in the store to the start Class - in future this could be used to store more than one start location
      setStart: (state, newStart) => {
        state.start = newStart.map(start => new Start(start))
      },
      // updatePostcode (state, journeyStart) { //duplicate?
      //   state.journeyStart = journeyStart
      // },
      setInputPostcode (state, value) {
        state.inputPostcode = value
      },
      setStartPostcode (state, value) {
        state.journeyStart = value
      }
    },
    getters: {
      freeSpaces: state => {
        return state.bays.filter(bays => !bays.charge); 
      },
      //getter to compare filtered bays with inputPostcode
      getInputPostcode: state => {
        return state.bays.filter( bay => bay.postcode.match(state.inputPostcode)) //changed item.postcode to bay.postcode - error item.postcode is undefined
      },
      //getter for startPostcode
      getStartPostcode: state => {
        return state.journeyStart
      },
      getStart: state => {
        return state.start
      }
      
      
    },
    //actions pass up to mutations
    actions: {
      loadInitialData: context => {
        context.commit('setBays', mockData.bays)
        context.commit('setStartPostcode', mockData.start)
      },
      updateInput: (context, value) => {
        context.commit('setInputPostcode', value )  //fire the mutation above
      },
      updateStart: (context, value) => {
        context.commit('setStartPostcode', value)
      }
    }
});



