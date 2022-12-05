import axios from 'axios'
import router from '@/router'

const state = () => ({
  myRecommendation: [],
  myLikeMovies: [],
  isLoading: false,
})

const mutations = {
  GET_RECOMMENDATION(state, data) {
    state.myRecommendation = data

  },
  GET_MY_LIKE_MOVIES(state, data) {
    state.myLikeMovies = data
  },
  START_ANALYZING(state) {
    state.isLoading = true
  },
  FINISH_ANALYZING(state) {
    state.isLoading = false
  }
}

const getters = {
  
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
  doAnalysis(context, user_pk) {
    context.commit('START_ANALYZING')
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/accounts/profile/${user_pk}/analysis/`,
      headers: headers
    })
    .then((response)=>{
      
      context.dispatch('getMyLikeMovies', user_pk)
      context.dispatch('getRecommendation', user_pk)
    })
    .catch((error)=>{
      context.commit('FINISH_ANALYZING')
      console.log(error)
    })
  },
  getRecommendation(context, user_pk) {
    context.commit('START_ANALYZING')
    const headers = {Authorization : `JWT ${localStorage.getItem('jwt')}`}
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/profile/${user_pk}/analysis/`,
      headers: headers
    })
    .then((response)=>{
                  
      // 장르
      const genres_values = Object.values(response.data.search_genres)
      const multi_genres_values = Object.values(response.data.search_multi_genres)
      const merge_genres = genres_values.concat(multi_genres_values)
      const genres = merge_genres.filter((item, pos)=>merge_genres.indexOf(item)===pos)
      const genres_list = genres.map((genre)=>{
        return ['genres', genre]
      })

      // 키워드
      const keywords_values = Object.values(response.data.search_keyword_list)
      const multi_keywords_values = Object.values(response.data.search_multi_keyword_list)
      const merge_keywords = keywords_values.concat(multi_keywords_values)
      const keywords = merge_keywords.filter((item, pos)=>merge_keywords.indexOf(item)===pos)
      const keywords_list = keywords.map((keyword)=>{
        return ['keywords', keyword]
      })

      // 회사
      const production_companies_values = Object.values(response.data.search_production_companies)
      const multi_production_companies_values = Object.values(response.data.search_production_companies)
      const merge_production_companies_values = production_companies_values.concat(multi_production_companies_values)
      const production_companies = merge_production_companies_values.filter((item, pos)=>merge_production_companies_values.indexOf(item)===pos)
      const companies_list = production_companies.map((company)=>{
        return ['companies', company]
      })

      // 장르_키워드_회사
      const genre_keyword_company = genres_list.concat(keywords_list.concat(companies_list))

      //랜덤 뽑기
      context.dispatch('random_pick', genre_keyword_company)
    })
    .catch((error)=>{
      console.log(error)
      context.commit('FINISH_ANALYZING')
    })
  },
  random_pick(context, genre_keyword_company) {
    let pick_list = []
    let pick_company = false
    while (pick_list.length < 3) {
      const pick = genre_keyword_company[Math.floor(Math.random() * genre_keyword_company.length)]
      if (!pick_list.includes(pick)) {
        if (pick[0] === 'companies') {
          if (pick_company === false) {
            pick_company = true
          } else {
            continue
          }
        }
        pick_list.push(pick)
      }
    }
    context.dispatch('getRecommendResult', {pick_list: pick_list, gkc: genre_keyword_company})
  },
  getRecommendResult(context, {pick_list, gkc}) {
    axios({
      method: 'get',
      url: `https://api.themoviedb.org/3/discover/movie?api_key=${process.env.VUE_APP_TMDB_API_KEY}&language=ko-KR&sort_by=popularity.desc&page=1&with_${pick_list[0][0]}=${pick_list[0][1]}&with_${pick_list[1][0]}=${pick_list[1][1]}&with_${pick_list[2][0]}=${pick_list[2][1]}`
    })
    .then((response) => {
      if (response.data.results.length === 0) {
        // 빈 배열일 경우 (주로 회사랑 조합되면 빈 배열) 다시 랜덤으로 키워드 장르 회사 빼오기
        context.dispatch('random_pick', gkc)
      } else {
        // console.log(context.state.myLikeMovies)
        // 좋아하는 영화 호출
        const valid_movie = response.data.results.filter((movie)=>{
          return movie.poster_path
        })

        let unique_movie = []
        valid_movie.forEach((movie)=>{
          let flag = false
          context.state.myLikeMovies.forEach((likemovie)=>{
            if (movie.id === likemovie.id) {
              flag = true
              return false
            }
          })
          if (flag === false) {
            unique_movie.push(movie)  
          }
        })
        context.commit('GET_RECOMMENDATION', unique_movie.slice(0, 3))
      }
      setTimeout(() => {
        context.commit('FINISH_ANALYZING')
      }, 1500)
    })
    .catch((error) => {
      console.log(error)
      context.commit('FINISH_ANALYZING')
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
