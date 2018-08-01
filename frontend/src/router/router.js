
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
    path: '/api/posts',
    redirect: '/',
  },
  {
    path: '/post',
    redirect: '/',
  },
  {
    path: '/posts',
    redirect: '/',
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
    meta: { requiresAuth: true },
    component: () => import('../components/compose/Compose.vue')
  },
  {
    path: '/posts/:pid',
    component: () => import('../components/post/Post.vue')
  },
  {
    path: '/api/posts/:pid',
    component: () => import('../components/post/Post.vue')
  }
]

// todo, 这里需要加上一些和admin相关的路由

const routes = [
  ...basicRoutes,
  ...otherSinglePage
]

export default routes
