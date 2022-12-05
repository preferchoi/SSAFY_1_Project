<template>
  <div>
    <div class="detail-main">
      <div class="topInfo">
        <div>
          <h1> {{ movie?.title }} ({{ movie?.released_date.substr(0, 4) }}) </h1>
        </div>
        <div class="miniInfo">
          <div class="detail-mini">
            <span>TMDB</span>
            {{ movie?.vote_average }}
          </div>&nbsp;
          <div class="detail-mini">
            <span>POPULARITY</span>
            {{ Math.round(movie?.popularity) }}
          </div>
        </div>
      </div>
      <hr>
      <div class="container">
        <DetailLeft :movie="movie" :movieDetail="movieDetail"/>
        <DetailRight :movie="movie" :movieDetail="movieDetail" :movieCredit="movieCredit"/>
      </div>
      <CreditSlider :movieCredit="movieCredit" title="출연진"/>
      <hr>
      <ReviewList :movie="movie"/>
      <hr>
      <Slider2 title='비슷한 영화' :movies="movieSimilar?.results"/>
    </div>
  </div>
</template>

<script>
import DetailLeft from '@/components/Detail/DetailLeft'
import DetailRight from '@/components/Detail/DetailRight'
import CreditSlider from '@/components/Detail/CreditSlider'
import Slider2 from '@/components/Slider2'
import ReviewList from '@/components/Review/ReviewList'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'MovieDetail',
  props: {
    movie: Object,
    movieDetail: Object,
    movieCredit: Object,
  },
  components: {
    DetailLeft,
    DetailRight,
    Slider2,
    CreditSlider,
    ReviewList,
  },
  methods: {
    ...mapActions('MovieDetail', [
      'getMovieVideo',
      'getMovieSimilar',
    ]),
  },
  computed: {
    ...mapState('MovieDetail', [
      'movieVideo',
      'movieSimilar',
    ])
  },

}
</script>

<style scoped>

  hr {
    background:rgb(226, 226, 226);
    height:1px;
    opacity: 0.2;
  }

  .detail-main .container {
    display: grid;
    grid-template-columns: 1fr 3fr;
    /* grid-template-columns: repeat(auto-fill, minmax(1fr, 3fr)); */
    grid-gap: 10px;
  }
  .detail-mini {
    font-size: 12px;
    border: 1px solid white;
    border-radius: 5px;
    width: fit-content;
    height: fit-content;
    padding: 5px 10px;
  }

  .topInfo {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: flex-end;
    margin: 0 1rem;
  }

  .miniInfo {
    display: flex;
    justify-content: space-between;
    align-items: center;
    text-align: center;
  }

  @media ( max-width: 1020px ) {
    .detail-main .container {
      grid-template-columns: 1fr 1fr;
    }
  }

  @media ( max-width: 800px ) {
    .detail-main .container {
      display: flex;
      flex-direction: column;
    }
  }


</style>