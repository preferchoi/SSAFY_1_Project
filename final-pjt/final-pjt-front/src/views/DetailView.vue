<template>
  <div>
    <section v-if="movie?.backdrop_path" class="movie-detail" :style="{
      background: `linear-gradient(135deg, rgba(0,0,0,0) 0%,rgba(0,0,0,0.65) 100%),
      url('https://www.themoviedb.org/t/p/original${movie?.backdrop_path}')`}">
      <div class="movie-box">
        <MovieDetail :movie="movie" :movieDetail="movieDetail" :movieCredit="movieCredit"/>
      </div>
    </section>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import MovieDetail from '@/components/Detail/MovieDetail'

export default {
  name: 'DetailView',
  components: {
    MovieDetail,
  },
  data() {
    return {
      movieId : this.$route.params.movieId
    }
  },
  methods: {
    ...mapActions('MovieDetail', [
      'getMovie',
      'getMovieDetail',
      'getMovieCredit',
      'getMovieVideo',
      'getMovieImage',
      'getMovieSimilar',
      'getMovieLike',
    ]),
    ...mapActions('Reviews', [
      'getReviews',
      'getRatingAverage'
    ]),
    ...mapActions('Accounts', [
      'allPageIn',
      'allPageOut',
    ])
  },
  computed: {
    ...mapState('MovieDetail', [
      'movie',
      'movieDetail',
      'movieCredit',
    ]),
  },
  created() {
    this.allPageIn()
  },
  mounted() {
    this.getMovie(this.movieId)
    this.getMovieDetail(this.movieId)
    this.getMovieCredit(this.movieId)
    this.getMovieImage(this.movieId)
    this.getMovieVideo(this.movieId)
    this.getMovieSimilar(this.movieId)
    this.getReviews(this.movieId)
    this.getMovieLike(this.movieId)
    this.getRatingAverage(this.movieId)
    setTimeout(() => {
    this.allPageOut()
    }, 1500)
  },
  beforeRouteUpdate(to, from, next) {
    this.movieId = to.params.movieId
    this.getMovie(this.movieId)
    this.getMovieDetail(this.movieId)
    this.getMovieCredit(this.movieId)
    this.getMovieImage(this.movieId)
    this.getMovieVideo(this.movieId)
    this.getMovieSimilar(this.movieId)
    this.getReviews(this.movieId)
    this.getMovieLike(this.movieId)
    this.getRatingAverage(this.movieId)
    next()
  }
}

</script>

<style>

  .movie-detail {
    background-size: 150%, cover!important;
    background-position: 50%, 50% !important;
    height: fit-content;
    padding-top: 10rem;
    display: flex;
  }

  .movie-box {
    border-radius: 30px;
    background-color: rgba( 0, 0, 0, 0.7 );
    margin: 100px auto;
    width: 80rem;
    height: fit-content;
    padding: 1rem;

  }
  @media ( max-width: 1400px ) {
    .movie-box {
      width: 95%
    }
  }


</style>