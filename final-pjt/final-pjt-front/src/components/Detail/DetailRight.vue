<template>
  <div class='rightbox'>
    <div class="right-grid">
      <div class="right-left">
        <div class="title-box">
          <h1>{{ movie?.title }}</h1>
          <div class="orange-box">
            <div class="released-box">{{movie?.released_date}}</div>
            <div class="runtime-box">⏰ {{ getRunningTime }}</div> 
          </div>
        </div>
        <div  class="tagline-box" v-if="movieDetail?.tagline">
          {{movieDetail?.tagline}}
        </div>
        <div class="genre-box">
          <div class="genre-tag" v-for="genre in movieDetail?.genres" :key="`${genre.id}box`">
            {{ genre?.name }}
          </div>
        </div>
        <hr>
        <div class="description-box">
          <div>
            <h1>세부정보</h1>
             <p>국가 : {{ movieDetail?.production_countries[0].name }}</p>
             <p>제작사 : {{ movieDetail?.production_companies[0].name }}</p>
             <p>언어 : {{ movieDetail?.spoken_languages[0].english_name }}</p>
             <p>흥행 수익 : {{ movieDetail?.revenue }}💰</p>
          </div>
        </div>
      </div>
      <div class="right-right">
        <DetailImage :movieImage="movieImage"/>
      </div>
    </div>
    <hr>
      <div>
        <h1>줄거리</h1>
        <p class="overview">{{ movie.overview }}</p>
      </div>
    <hr>
  </div>

        
    

</template>

<script>
import DetailImage from '@/components/Detail/DetailImage'

import { mapState, mapGetters } from 'vuex'

export default {
  name: 'DetailRight',
  components: {
    DetailImage,
  },
  props: {
    movie: Object,
    movieDetail: Object,
    movieImage: Object,
  },
  computed: {
    ...mapState('MovieDetail', [
      'genreList'
    ]),
    ...mapGetters('MovieDetail', [
      'getRunningTime'
    ])
  }
}
</script>

<style scoped>
  .rightbox {
    padding: 0 10px;
    text-align: left;
  }

  .right-grid {
    display: grid;
    grid-template-columns: 3fr 2fr;
    grid-gap: 10px;
  }

  h1 {
    margin: 5px 5px;
  }

  hr {
    background:rgb(226, 226, 226);
    height:1px;
    margin-top:20px;
    opacity: 0.2;
  }
  .title-box {
    display: flex;
    justify-content: flex-start;
    flex-wrap: wrap;
    align-items: center;
    padding: 5px;

  }

  .tagline-box {
    margin: 0 10px
  }
  .title-box h1 {
    font-size: 40px;
    margin: 5px 5px 5px 5px
  }

  .released-box {
    background-color: rgba(255, 145, 0, 0.8);
    border-radius: 10px;
    margin: 5px;
    width: fit-content;
    height: fit-content;
    padding: 5px 10px;
  }

  .runtime-box {
    background-color: rgba(255, 145, 0, 0.8);
    border-radius: 10px;
    margin: 5px;
    width: fit-content;
    height: fit-content;
    padding: 5px 10px;
  }

  .genre-box {
    display: flex;
    justify-content:flex-start;
    text-align: center;
    margin-top: 10px;
  }
  .genre-tag {
    background-color: rgba(97, 97, 97, 0.5);
    border-radius: 10px;
    margin: 0 5px;
    width: fit-content;
    height: fit-content;
    padding: 5px 10px;
  }

  .orange-box {
    display: inline-flex;
  }

  .description-box h1 {
    margin-bottom: 3px 3px;
  }
  .description-box p {
    margin: 0 10px;
  }

  .overview {
    margin: 0 10px
  }

  .right-right {
    margin: auto;
    padding: 10px;
  }

  @media ( max-width: 800px ) {
    .title-box h1 {
    font-size: 30px;
    }

  }

  @media ( max-width: 1020px ) {
    .right-grid {
      display: flex;
      flex-direction: column;
    }

  }
  </style>