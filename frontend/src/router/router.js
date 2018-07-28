
// 基本的router

const basicRouterOptions = [
  {
    path: '/', 
    component: 'Home'
  },
  // 下面这四个路由都应该转到home下面
  {
    path: '/home',
    redirect: '/',
    component: 'Home'
  },
  {
    path: '/post',
    redirect: '/',
    component: 'Home'
  },
  {
    path: '/posts',
    redirect: '/',
    component: 'Home'
  },
  {
    path: '/login',
    component: 'Login'
  },
  {
    path: '/register',
    component: 'Register'
  },
  {
    path: '/layout',
    component: 'MyLayout'
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
        return import(`../components/${route.component}`)
      }
    }
  }
)

// 这些我是用单页面的形式表示的。
const otherSinglePage = [
  {
    path: '/category',
    component: () => import('../components/category/Category.vue')
  },
  {
    path: '/tag',
    component: () => import('../components/tag/Tag.vue')
  },
  {
    path: '/about',
    component: () => import('../components/about/About.vue')
  },
  {
    path: '/profile',
    component: () => import('../components/profile/Profile.vue')
  },
  {
    path: '/compose',
    component: () => import('../components/compose/Compose.vue')
  },
  {
    path: '/post/:pid',
    component: () => import('../components/post/Post.vue')
  }
]

// todo, 这里需要加上一些和admin相关的路由

const routes = [
  ...basicRoutes,
  ...otherSinglePage
]

export default routes
