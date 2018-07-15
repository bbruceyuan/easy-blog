
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
// 这里功能基本和router上的路由拦截器功能一样，不过主要是针对后端
// 因为有些api不需要改变浏览器地址栏
axios.interceptors.request.use((config) => {
  if (store.state.token) {
    config.headers.Authorization = `token ${store.state.token}`
  }
  return config
}, (error) => {
  return Promise.reject(error)
})


// http response 拦截器
// 这相对来说是针对后端的做的拦截器
axios.interceptors.response.use((response) => {
  return response;
}, (error) => {
  if (error.response) {
    switch (error.response.status) {
      // axios拦截器，401状态时跳转登录页并清除token
      // 401 是没有授权的意思
      case 401:
        store.commit(types.LOGOUT)
        router.replace('/login')
        break
      }
  }
  return Promise.reject(error.response.data)
})

export default axios
