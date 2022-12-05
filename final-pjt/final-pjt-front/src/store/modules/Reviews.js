import axios from 'axios'
import router from '@/router'

const state = () => ({
  reviews: [],
  isReviewLike: null,
  ratingAverage: null,
})

const mutations = {
  GET_REVIEWS(state, reviews) {
    state.reviews = reviews
  },
  IS_REVIEW_LIKE(state, data) {
    state.isReviewLike = data
  },
  GET_RATING_AVERAGE(state, data) {
    state.ratingAverage = data
  }
}

const getters = {
  
}

const actions = {
  getReviews(context, movieId) {

    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/${movieId}/reviews/`,
      headers: headers
    })
    .then((response)=>{
      context.commit('GET_REVIEWS', response.data)
    })
    .catch((error)=>{
      console.log(error)
    })
  },
  createReview(context, {movieId, review}) {
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/movies/${movieId}/reviews/`,
      data: review,
      headers: headers
    })
    .then((response)=>{
      console.log(response)
      context.dispatch('getReviews', movieId)
      context.dispatch('getRatingAverage', movieId)
    })
    .catch((error)=>{
      console.log(error)
    })
  },
  updateReview(context, {movieId, reviewId, review}) {
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'put',
      url: `http://127.0.0.1:8000/movies/reviews/${reviewId}/`,
      data: review,
      headers: headers
    })
    .then((response)=>{
      console.log(response)
      context.dispatch('getReviews', movieId)
      context.dispatch('getRatingAverage', movieId)
    })
    .catch((error)=>{
      console.log(error)
    })
  },
  deleteReview(context, {movieId, reviewId}) {
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'delete',
      url: `http://127.0.0.1:8000/movies/reviews/${reviewId}/`,
      headers: headers
    })
    .then((response)=>{
      console.log(response)
      context.dispatch('getReviews', movieId)
      context.dispatch('getRatingAverage', movieId)
    })
    .catch((error)=>{
      console.log(error)
    })
  },

  getReviewLike(context, reviewId) {
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/${reviewId}/like_review/`,
      headers: headers
    })
    .then((response)=>{
      context.commit('IS_REVIEW_LIKE', response.data)
    })
    .catch((error)=>{
      console.log(error)
    })
  },

  reviewLike(context, reviewId) {
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/movies/${reviewId}/like_review/`,
      headers: headers
    })
    .then((response)=>{
      context.commit('IS_REVIEW_LIKE', response.data)
    })
    .catch((error)=>{
      console.log(error)
    })
  },

  getRatingAverage(context, movieId) {
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/${movieId}/get_our_rating/`,
      headers: headers
    })
    .then((response)=>{
      console.log(response)
      context.commit('GET_RATING_AVERAGE', response.data)
    })
    .catch((error)=>{
      console.log(error)
    })
  }
}

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters,
}