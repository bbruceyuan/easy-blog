
// axios 基本配置

import axios from 'axios'
import store from './store'
import router from './router'
import * as types from './store/mutationTypes'

axios.defaults.baseURL = 'http://127.0.0.1:5000'
axios.defaults.auth = {
  username: '',
  password: ''
}

// http request 拦截器


// http response 拦截器

