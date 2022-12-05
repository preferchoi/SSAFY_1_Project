
import axios from 'axios'


const state = {
  nowMovies : [],
  popularMovies : [],
  trendMovies : [],
  topMovies : [],
  searchMovies: [],
}

const getters = {
 }

const mutations = {
  GET_NOW_MOVIES (state, data) {
    state.nowMovies = data
  },
  GET_POPULAR_MOVIES (state, data) {
    state.popularMovies = data
  },
  GET_TREND_MOVIES (state, data) {
    state.trendMovies = data
  },
  GET_TOP_MOVIES (state, data) {
    state.topMovies = data
  },
  GET_SEARCH_MOVIES (state, data) {
    state.searchMovies = data
  },
  CLEAR_SEARCH (state) {
    state.searchMovies = []
  }
}

const actions = {
  getNowMovies(context) {
    axios({
      method: 'get',
      url: `https://api.themoviedb.org/3/movie/now_playing?api_key=${process.env.VUE_APP_TMDB_API_KEY}&language=ko-KR`
    })
    .then(response => {
      const movieList = response.data.results.filter((movie)=>{
        return (movie.overview && movie.backdrop_path)
      })
      context.commit('GET_NOW_MOVIES', movieList)
    })
    .catch(error => {
      console.log(error)
    })
  },
  getPopularMovies(context) {
    axios({
      method: 'get',
      url: `https://api.themoviedb.org/3/movie/popular?api_key=${process.env.VUE_APP_TMDB_API_KEY}&language=ko-KR`
    })
    .then(response => {
      const movieList = response.data.results.filter((movie)=>{
        return (movie.overview && movie.backdrop_path)
      })
      context.commit('GET_POPULAR_MOVIES', movieList)
    })
    .catch(error => {
      console.log(error)
    })
  },
  getTrendMovies(context) {
    axios({
      method: 'get',
      url: `https://api.themoviedb.org/3/movie/top_rated?api_key=${process.env.VUE_APP_TMDB_API_KEY}&language=ko-KR`
    })
    .then(response => {
      const movieList = response.data.results.filter((movie)=>{
        return (movie.overview && movie.backdrop_path)
      })
      context.commit('GET_TREND_MOVIES', movieList)
    })
    .catch(error => {
      console.log(error)
    })
  },
  
  getTopMovies(context) {
    axios({
      method: 'get',
      url: `https://api.themoviedb.org/3/trending/movie/week?api_key=${process.env.VUE_APP_TMDB_API_KEY}&language=ko-KR`
    })
    .then(response => {
      const topMovieList = response.data.results.slice(0, 3)
      const topMovies = []
      topMovieList.forEach((movie)=>{
        axios({
          method: 'get',
          url: `https://api.themoviedb.org/3/movie/${movie?.id}/videos?api_key=${process.env.VUE_APP_TMDB_API_KEY}`
        })
        .then((response)=>{
          const newMovie = {
            movieInfo: movie,
            movieVideo: response.data.results[0].key
          }
          topMovies.push(newMovie)
        })
        .catch((error)=>{
          console.log(error)
        })
      })
      context.commit('GET_TOP_MOVIES', topMovies)
    })
    .catch(error => {
      console.log(error)
    })
  },

  getSearchMovies(context, search) {
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/movies/search/`,
      headers: headers,
      data: {keyword: search},
    })
    .then((response)=>{
      context.commit('GET_SEARCH_MOVIES', response.data)
    })
    .catch((error)=>{
      console.log(error)
    })
  },
  clearSearch(context) {
    context.commit(CLEAR_SEARCH)
  }

}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
}