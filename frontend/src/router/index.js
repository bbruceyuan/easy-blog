import Vue from 'vue'
import Router from 'vue-router'
import store from '../store'
// import iView from 'iview'
import axios from '../http'

import routes from './router'
import { LOGIN } from '../store/mutationTypes'

Vue.use(Router)

const router = new Router({
  routes,
  mode: 'history'
})

// 刷新页面时重新赋值 token
if (localStorage.getItem('token')) {
  let payload = {
    token: localStorage.token,
    loginUser: localStorage.loginUser
  }
  store.commit(LOGIN, payload)
}

// 请求前判断是否需要加token
router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (localStorage.getItem('token') && localStorage.getItem('loginUser')) {
      let payload = {
        token: localStorage.getItem('token'),
        loginUser: localStorage.getItem('loginUser')
      }
      store.commit(LOGIN, payload)
      // 因为我们判断没有密码的时候，就使用token认证
      axios.defaults.auth = {
        username: store.state.token,
        password: ''
      }
      next()
    } else {
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      })
    }
  } else {
    // 暂时不需要，影响体验
    // iView.LoadingBar.start()
    next()
  }
})

// 每次请求结束，这个loading要结束
// 暂时不需要，感觉影响体验
// router.afterEach((to, from, next) => {
//   iView.LoadingBar.finish()
//   next()
// })

export default router
