import axios from 'axios'
import router from '@/router'

const state = {
  user_pk: null,
  my_pk: null,
  myLikeMovies: null,
  myRatingMovies: null,
  myProfile: null,
  navProfile: null,
  followData: null,
}

const getters = {

}

const mutations = {
  GET_MY_LIKE_MOVIES(state, data) {
    state.myLikeMovies = data
  },
  GET_MY_RATING_MOVIES(state, data) {
    state.myRatingMovies = data
  },
  GET_MY_PROFILE(state, data) {
    state.myProfile = data
  },
  GET_USER_PK(state, data) {
    state.user_pk = data
  },
  GET_NAV_PROFILE(state, data) {
    state.navProfile = data
    state.my_pk = data.id 
  },
  FOLLOW(state, data) {
    state.followData = data
  },
}

const actions = {
  getMyLikeMovies(context, user_pk) {
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/${user_pk}/like_movie/`,
      headers: headers
    })
    .then((response)=>{
      context.commit('GET_MY_LIKE_MOVIES', response.data)
    })
    .catch((error)=>{
      console.log(error)
    })
  },
  getMyRatingMovies(context, user_pk) {
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/${user_pk}/write_review/`,
      headers: headers
    })
    .then((response)=>{
      console.log(response)
      context.commit('GET_MY_RATING_MOVIES', response.data)
    })
    .catch((error)=>{
      console.log(error)
    })
  },
  getMyProfile(context, username) {
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/profile/${username}/`,
      headers: headers
    })
    .then((response)=>{
      context.commit('GET_MY_PROFILE', response.data)
      context.commit('GET_USER_PK', response.data.id)
      context.dispatch('getMyLikeMovies', response.data.id)
      context.dispatch('getMyRatingMovies', response.data.id)
      context.dispatch('getFollow', response.data.id)
    })
    .catch((error)=>{
      console.log(error)
    })
  },
  getNavProfile(context, username) {
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/profile/${username}/`,
      headers: headers
    })
    .then((response)=>{
      context.commit('GET_NAV_PROFILE', response.data)
    })
    .catch((error)=>{
      console.log(error)
    })
  },
  updateProfile(context, {form, username}) {
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`, 'Content-Type': 'multipart/form-data'}
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/accounts/profile/${username}/`,
      headers: headers,
      data: form,
    })
    .then((response)=>{
      context.commit('GET_MY_PROFILE', response.data)
      context.commit('GET_NAV_PROFILE', response.data)
    })
    .catch((error)=>{
      console.log(error)
    })
  },
  getFollow(context, user_pk) {
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/${user_pk}/follow/`,
      headers: headers
    })
    .then((response)=>{
      console.log(response)
      context.commit('FOLLOW', response.data)
    })
    .catch((error)=>{
      console.log(error)
    })
  },
  doFollow(context, user_pk) {
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/accounts/${user_pk}/follow/`,
      headers: headers
    })
    .then((response)=>{
      context.commit('FOLLOW', response.data)
    })
    .catch((error)=>{
      console.log(error)
    })
  },
  changeBackdrop(context, {backdrop_path, username}) {
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/accounts/profile/${username}/`,
      headers: headers,
      data: {backdrop_path: backdrop_path}
    })
    .then((response)=>{
      context.commit('GET_MY_PROFILE', response.data)
    })
    .catch((error)=>{
      console.log(error)
    })
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
}