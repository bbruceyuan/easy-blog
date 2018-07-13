
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

const routes = [
  ...basicRoutes
]

export default routes
