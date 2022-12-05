<template>
  <div class="container">
    <div class="index">
      <section class="main-box">
        <Carousel :movies="topMovies"/>
      </section>
      <section class="slide-box">
        <Slider title="🎥 상영중인 영화" :movies="nowMovies" />
        <Slider title="⭐ 인기있는 영화" :movies="popularMovies" />
        <Slider title="🏆 높은평점 영화" :movies="trendMovies" />
      </section>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import Slider from '@/components/Slider'
import Carousel from '@/components/Carousel'


export default {
  name: 'HomeView',
  components: {
    Slider,
    Carousel,
  },
  computed: {
    ...mapState('Movies', [
      'nowMovies', 
      'popularMovies', 
      'trendMovies',
      'topMovies',
    ]),
    ...mapState('Accounts', [
      'username'
    ])
  },
  methods: {
    ...mapActions('Profile', [
      'getNavProfile',
    ]),
    ...mapActions('Accounts', [
      'allPageIn',
      'allPageOut',
    ])
  },
  created() {
    this.allPageIn()
  },
  mounted() {
    if (this.username) {
      this.getNavProfile(this.username)
    }
    setTimeout(() => {
    this.allPageOut()
    }, 1500)
  },
}
</script>

<style scoped>
  .container {
    display: flex;
    flex-direction: center;
    justify-content: center;
    margin-bottom: 5rem;
  }
  .index {
    padding-top: 6rem;
    width: 100%;
  }
  .slide-box {
    margin: auto;
    width: 90%;
  }
  .main-box {
    width: 100%;
  }
</style>