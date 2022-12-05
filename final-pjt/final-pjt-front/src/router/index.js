import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RecommendationView from '@/views/RecommendationView'
import SearchView from '@/views/SearchView'
import ProfileView from '@/views/ProfileView'
import SignUpView from '@/views/SignUpView'
import DetailView from '@/views/DetailView'
import LogInView from '@/views/LogInView'
import store from "@/store"

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/detail/:movieId',
    name: 'DetailView',
    component: DetailView
  },
  {
    path: '/recommendation',
    name: 'RecommendationView',
    component: RecommendationView
  },
  {
    path: '/search',
    name: 'SearchView',
    component: SearchView
  },
  {
    path: '/profile/:username',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('jwt')
  if (!token && (to.name === "DetailView" ||
      to.name === "RecommendationView" ||
      to.name === "SearchView" ||
      to.name === "ProfileView")) {
        alert('로그인이 필요한 서비스 입니다.')
        next({ name: "LogInView"})
      }
  if (from.name === 'SearchView') {
    store.commit('Movies/CLEAR_SEARCH')
    //검색 페이지에서 나왔을 때 스토어 값 초기화
  }
  next()
})

export default router

