import Vue from 'vue'
import Vuex from 'vuex'
import Movies from './modules/Movies'
import MovieDetail from './modules/MovieDetail'
import Recommendation from './modules/Recommendation'
import Reviews from './modules/Reviews'
import Comments from './modules/Comments'
import Accounts from './modules/Accounts'
import Profile from './modules/Profile'


Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    Movies,
    MovieDetail,
    Recommendation,
    Reviews,
    Accounts,
    Comments,
    Profile,
  }
})
