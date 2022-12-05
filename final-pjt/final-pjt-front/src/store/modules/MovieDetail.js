
import router from '@/router'
import axios from 'axios'

const state = {
  movie: null,
  movieDetail: null,
  movieVideo: null,
  movieCredit: null,
  movieSimilar: null,
  movieImage: null,
  isMovieLike: null,
}

const getters = {
  getRunningTime () {
    return `${Math.round(Number(state.movieDetail?.runtime)/60)}시간 ${Number(state.movieDetail?.runtime)%60}분` 
  }
 }

const mutations = {
  GET_MOVIE(state, data) {
    state.movie = data
  },
  GET_MOVIE_VIDEO(state, data) {
    state.movieVideo = data
  },
  GET_MOVIE_DETAIL(state, data) {
    state.movieDetail = data
  },
  GET_MOVIE_CREDIT (state, data) {
    state.movieCredit = data
  },
  GET_MOVIE_SIMILAR (state, data) {
    state.movieSimilar = data
  },
  GET_MOVIE_IMAGE (state, data) {
    state.movieImage = data
  },
  IS_MOVIE_LIKE (state, data) {
    state.isMovieLike = data
  }
}

const actions = {
  getMovie(context, movieId) {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/${movieId}/`,
    })
    .then((response)=>{
      context.commit('GET_MOVIE', response.data)
    })
    .catch((error)=>{
      alert('데이터베이스에 영화 정보가 없습니다.')
      router.push({name: 'HomeView' })
      console.log(error)
    })
  },

  getMovieVideo(context, movieId) {
    axios({
      method: 'get',
      url: `https://api.themoviedb.org/3/movie/${movieId}/videos?api_key=${process.env.VUE_APP_TMDB_API_KEY}`
    })
    .then(response => {
      context.commit('GET_MOVIE_VIDEO', response.data.results[0])
    })
    .catch(error => {
      console.log(error)
    })
  },
  getMovieDetail(context, movieId) {
    axios({
      method: 'get',
      url: `https://api.themoviedb.org/3/movie/${movieId}?api_key=${process.env.VUE_APP_TMDB_API_KEY}&language=ko-KR`
    })
    .then(response => {
      context.commit('GET_MOVIE_DETAIL', response.data)
    })
    .catch(error => {
      console.log(error)
    })
  },
  getMovieCredit(context, movieId) {
    axios({
      method: 'get',
      url: `https://api.themoviedb.org/3/movie/${movieId}/credits?api_key=${process.env.VUE_APP_TMDB_API_KEY}&language=ko-KR`
    })
    .then(response => {
      context.commit('GET_MOVIE_CREDIT', response.data)
    })
    .catch(error => {
      console.log(error)
    })
  },
  getMovieSimilar(context, movieId) {
    axios({
      method: 'get',
      url: `https://api.themoviedb.org/3/movie/${movieId}/similar?api_key=${process.env.VUE_APP_TMDB_API_KEY}&language=ko-KR`
    })
    .then(response => {
      context.commit('GET_MOVIE_SIMILAR', response.data)
    })
    .catch(error => {
      console.log(error)
    })
  },
  getMovieImage(context, movieId) {
    axios({
      method: 'get',
      url: `https://api.themoviedb.org/3/movie/${movieId}/images?api_key=${process.env.VUE_APP_TMDB_API_KEY}`
    })
    .then(response => {
      context.commit('GET_MOVIE_IMAGE', response.data)
    })
    .catch(error => {
      console.log(error)
    })
  },

  getMovieLike(context, movieId) {
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/${movieId}/like_movie/`,
      headers: headers
    })
    .then((response)=>{
      context.commit('IS_MOVIE_LIKE', response.data)
    })
    .catch((error)=>{
      console.log(error)
    })
  },

  movieLike(context, movieId) {
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/movies/${movieId}/like_movie/`,
      headers: headers
    })
    .then((response)=>{
      context.commit('IS_MOVIE_LIKE', response.data)
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






