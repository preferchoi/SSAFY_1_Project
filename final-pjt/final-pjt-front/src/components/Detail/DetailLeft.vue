<template>
  <div class="flex-div">
    <img :src="`https://www.themoviedb.org/t/p/original${movie?.poster_path}`" alt="" class="poster">
    <div class="starlike">
      <div class="star-box">
        <span>평점<i class="fa-regular fa-star"></i>
        {{ ratingAverage?.our_rating }}</span>
      </div>
      <div class="like-box" @click="vueLikeMovie">
        <span>좋아요
          <i v-if="isMovieLike?.is_movie_like" class="fa-solid fa-heart"></i>
          <i v-else class="fa-regular fa-heart"></i>
          &nbsp;{{ isMovieLike?.movie_like_count }}</span>
      </div>
    </div>
    <star-rating 
      :rating="ratingAverage?.our_rating" 
      :star-size="50" 
      :glow="10"
      :read-only="true" 
      :show-rating="false"
      :increment="0.01">
    </star-rating>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

import StarRating from 'vue-star-rating'

export default {
  name: 'DetailLeft',
  components: {
    StarRating
  },
  props: {
    movie: Object,
    movieDetail: Object,
  },
  computed: {
    ...mapState('MovieDetail', [
      'isMovieLike',
    ]),
    ...mapState('Reviews', [
      'ratingAverage',
    ]),
  },
  methods: {
    ...mapActions('MovieDetail', [
      'movieLike'
    ]),
    vueLikeMovie() {
      this.movieLike(this.movie.id)
    }
  }
}
</script>

<style scoped>
  .flex-div {
    text-align: center;
    margin: auto;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .poster {
    border-radius: 20px;
    filter: drop-shadow(5px 5px 5px rgb(68, 68, 68));
    width: 100%;
  }
  .vue-star-rating {
    display: flex;
    justify-content: center;
    text-align: center;
  }

  .starlike {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .star-box {
    border-radius: 5px;
    margin: 5px 5px;
    color: black;
    font-weight: bold;
    padding: 3px 10px;
    background-color: rgba(255, 196, 0, 0.8);
  }

  .like-box {
    border-radius: 5px;
    margin: 5px 5px;
    font-weight: bold;
    padding: 3px 10px;
    background-color: rgba(248, 63, 63, 0.8);
  }

  .like-box:hover {
    background-color: rgba(214, 52, 52, 0.8);
  }

  @media ( max-width: 800px ) {
    .poster {
      width: 450px
    }
  }
</style>