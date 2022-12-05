import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import "swiper/css/swiper.css"
import Dropdown from 'vue-2-dropdown'
import 'vue-2-dropdown/dist/vue-2-dropdown.css';

Vue.use(Dropdown)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
