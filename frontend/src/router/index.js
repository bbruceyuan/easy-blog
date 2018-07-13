import Vue from 'vue'
import Router from 'vue-router'
// import store from '../store'
// import iView from 'iview'
// import axios from '../http'

import routes from './router'
// import { LOGIN } from '../store/mutationTypes'

Vue.use(Router)

const router = new Router({
  routes,
  mode: 'history'
})


export default router
