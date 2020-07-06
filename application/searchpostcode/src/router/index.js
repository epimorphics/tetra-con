import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import resultsView from '@/views/resultsView.vue'
import indivbayView from '@/views/indivbayView.vue'
import map from '@/components/map.vue'
import distanceView from '@/views/distanceView.vue'


Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/results',
    name: 'resultsView',
    component: resultsView
  },
  {
    //add dynamic segments
    path: '/indivbay/:bayId',
    name: 'indivbay',
    component: indivbayView
  },
  {
    path: '/distance',
    name: 'distance',
    component: distanceView
  },
  {
    path: '/map',
    name: 'map',
    component: map
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  
  routes
})

export default router

// const app = new Vue({
//   routes
// }).$mount('#app')