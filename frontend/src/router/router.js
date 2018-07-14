
// 基本的router

const basicRouterOptions = [
  {
    path: '/', 
    component: 'Home'
  },
  {
    path: '/login',
    component: 'Login'
  },
  {
    path: '*', 
    component: 'NotFound'
  }
]

const basicRoutes = basicRouterOptions.map(
  route => {
    return {
      ...route,
      component: () => {
        import(`@/components/${route.component}`)
      }
    }
  }
)

// todo, 这里需要加上一些和admin相关的路由

const routes = [
  ...basicRoutes
]

export default routes
