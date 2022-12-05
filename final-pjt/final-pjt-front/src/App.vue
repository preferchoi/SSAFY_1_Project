<template>
  <div id="app">
    <AllSpinner v-if="allIsLoading"/>
    <NavBar/>
    <main>
      <router-view/>
    </main>
    <Footer/>
  </div>
</template>

<script>

import NavBar from '@/components/NavBar'
import Footer from '@/components/Footer'
import AllSpinner from '@/components/AllSpinner'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'App',
  components: {
    NavBar,
    Footer,
    AllSpinner,
  },
  computed: {
    ...mapState('Accounts', [
      'username',
      'allIsLoading',
    ])
  },
  methods: {
    ...mapActions('Movies', [
      'getNowMovies', 
      'getPopularMovies', 
      'getTrendMovies',
      'getTopMovies',

    ]),
    ...mapActions('Accounts', [
      'allPageIn',
      'allPageOut',
    ]),
    ...mapActions('Profile', [
      'getNavProfile'
    ])
  },
  created() {
    this.getNowMovies()
    this.getPopularMovies()
    this.getTrendMovies()
    this.getTopMovies()
    if (this.username) {
      this.getNavProfile(this.username)
    }
  },
  watch: {
    $route() {
      window.scrollTo(0, 0);
    },
  },
}
</script>


<style>
@import url('https://fonts.googleapis.com/css2?family=Dhurjati&family=Noto+Sans+KR:wght@300;400;500;700;900&family=Yanone+Kaffeesatz:wght@200;300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');


#app {
  font-family: 'Noto Sans KR', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  position: relative;
  text-align: center;
  color: white;
  min-height : 100%;
  padding-bottom: 1px;
}
main {
  margin-top: 50px;
}

body {
  background-color: #1f1f1f;
  height: 100%;
}

html {
  scroll-behavior: smooth;
  height: 100%;
  
}

a {
  text-decoration: none;
}



</style>
