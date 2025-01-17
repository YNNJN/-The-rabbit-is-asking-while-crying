import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Community from '../views/Community.vue'
import SignupView from '../views/accounts/SignupView.vue'
import LoginView from '../views/accounts/LoginView.vue'
import UserPageView from '../views/UserPageView.vue'
import PickMovieView from '../views/PickMovieView.vue'
import ScoreView from '../views/community/ScoreView.vue'
// import ReviewListView from '../views/articles/ReviewListView.vue'
// import ReviewCreateView from '../views/articles/ReviewCreateView.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/community',
    name: 'Community',
    component: Community
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
    path: '/movies/pickmovie',
    name: 'PickMovie',
    component: PickMovieView
  },
  {
    path: '/community/score',
    name: 'Score',
    component: ScoreView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
