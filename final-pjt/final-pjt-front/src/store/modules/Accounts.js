
import axios from 'axios'
import router from '@/router'

const state = {
  signUpErrorMessage: null,
  logInErrorMessage: null,
  token: localStorage.getItem('jwt') || null,
  username: localStorage.getItem('username') || null,
  isLoading: false,
  allIsLoading: false,
}

const getters = {
  isLoggedIn(state) {
    return state.token ? true : false
  }
 }

const mutations = {
  SIGNUP_ERROR_MESSAGE(state, message) {
    state.signUpErrorMessage = message
  },
  DEL_MESSAGE(state) {
    state.signUpErrorMessage = null
  },
  LOGIN_ERROR_MESSAGE(state, message) {
    state.logInErrorMessage = message
  },
  UPDATE_TOKEN(state, {token, username}) {
    state.token = token,
    state.username = username
  },
  DELETE_TOKEN(state) {
    state.token = null,
    state.username = null
  },
  PAGE_IN(state) {
    state.isLoading = true
  },
  PAGE_OUT(state) {
    state.isLoading = false
  },
  ALL_PAGE_IN(state) {
    state.allIsLoading = true
  },
  ALL_PAGE_OUT(state) {
    state.allIsLoading = false
  }
}

const actions = {
  signUp(context, credentials) {
    console.log(context)
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/signup/',
      data: credentials,
    })
    .then((response)=>{
      console.log(response)
      context.dispatch('logIn', credentials) // 회원가입 후 바로 로그인
    })
    .catch((error)=>{
      context.commit('SIGNUP_ERROR_MESSAGE', '이미 사용중인 아이디입니다.')
      console.log(error)
    })
  },
  delMessage(context) {
    context.commit('DEL_MESSAGE')
  },
  pageIn(context) {
    context.commit('PAGE_IN')
  },
  pageOut(context) {
    context.commit('PAGE_OUT')
  },
  allPageIn(context) {
    context.commit('ALL_PAGE_IN')
  },
  allPageOut(context) {
    context.commit('ALL_PAGE_OUT')
  },

  logIn(context, credentials) {
    context.commit('LOGIN_ERROR_MESSAGE', null)
    console.log(context)
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/token/',
      data: credentials,
    })
    .then((response)=>{
      console.log(response)
      localStorage.setItem('jwt', response.data.access)
      localStorage.setItem('username', credentials.username)
      context.commit('UPDATE_TOKEN', 
      {token: response.data.access, username: credentials.username})
      router.push({ name: 'HomeView'}) 
    })
    .catch((error)=>{
      console.log(error)
      context.commit('LOGIN_ERROR_MESSAGE', '잘못된 로그인 정보입니다.')
    })
  },

  logOut(context) {
    console.log(context)
    localStorage.removeItem('jwt')
    localStorage.removeItem('username')
    context.commit('DELETE_TOKEN')
    router.push({ name: 'HomeView'}).catch(()=>{})
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
}