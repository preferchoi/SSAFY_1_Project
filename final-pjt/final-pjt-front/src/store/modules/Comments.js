import axios from 'axios'
import router from '@/router'

const state = () => ({
  comments: [],
})

const mutations = {
  GET_COMMENTS(state, comments) {
    state.comments = comments
  }
}

const getters = {
  
}

const actions = {
  getComments(context, reviewId) {
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/${reviewId}/comments/`,
      headers: headers
    })
    .then((response)=>{
      context.commit('GET_COMMENTS', response.data)
    })
    .catch((error)=>{
      console.log(error)
    })
  },
  createComment(context, {reviewId, comment}) {
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/movies/${reviewId}/comments/`,
      data: comment,
      headers: headers
    })
    .then((response)=>{
      console.log(response)
      context.dispatch('getComments', reviewId)
    })
    .catch((error)=>{
      console.log(error)
    })
    },
  updateComment(context, {commentId, reviewId, comment}) {
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'put',
      url: `http://127.0.0.1:8000/movies/comments/${commentId}/`,
      data: comment,
      headers: headers
    })
    .then((response)=>{
      console.log(response)
      context.dispatch('getComments', reviewId)
    })
    .catch((error)=>{
      console.log(error)
    })
  },
  deleteComment(context, {commentId, reviewId}) {
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'delete',
      url: `http://127.0.0.1:8000/movies/comments/${commentId}/`,
      headers: headers
    })
    .then((response)=>{
      console.log(response)
      context.dispatch('getComments', reviewId)
    })
    .catch((error)=>{
      console.log(error)
    })
  },
}

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters,
}