import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import SignupView from '../views/accounts/SignupView.vue'
import LoginView from '../views/accounts/LoginView.vue'
import UserPageView from '../views/UserPageView.vue'
import ArticleListView from '../views/articles/ArticleListView.vue'
import ArticleCreateView from '../views/articles/ArticleCreateView.vue'


Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: SignupView
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/accounts/userpage',
    name: 'Userpage',
    component: UserPageView
  },
  {
    path: '/articles',
    name: 'List',
    component: ArticleListView
  },
  {
    path: '/articles/create',
    name: 'New',
    component: ArticleCreateView,
    beforeEnter: (to, from, next) => {
      if (!Vue.$cookies.isKey('auth-token')) {
        next({ name: 'Login' })
      } else { next() }
    }
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
