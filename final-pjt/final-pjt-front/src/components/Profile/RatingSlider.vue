<template>
  <section>
    <h2>⭐ {{ this.$route.params.username }}님이 평가한 영화</h2>
    <swiper v-if="movies?.length !==0" class="swiper" :options="swiperOptions">
      <swiper-slide
        v-for="movie in movies"
        :key="movie?.id">
        <div class="movie-item">
          <router-link :to="{ name: 'DetailView', params: { movieId: movie?.id } }">
          <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movie?.poster_path}`" alt="" class="poster">
          <span class="title">{{ movie.title }}</span> 
          </router-link>
        </div>
      </swiper-slide>
    </swiper>
    <div class="noRating" v-else>아직 별점⭐을 남긴 영화가 없습니다.</div>
  </section>
</template>

<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'

export default {
  name: "Slider",
  props: {
    movies: Array,
  },
  components : {
    Swiper,
    SwiperSlide
  },
  data() {
    return {      
      swiperOptions: {
        // mousewheel: true,
        spaceBetween: 30,
        // autoplay: {
        //   delay: 2500,
        //   disableOnInteraction: false
        // },
        loopFillGroupWithBlank: true,
        breakpoints: {
          2000: {
            slidesPerView: 6,
            spaceBetween: 20
          },
          1580: {
            slidesPerView: 5,
            spaceBetween: 20
          },
          1160: {
            slidesPerView: 4,
            spaceBetween: 20
          },
          900: {
            slidesPerView: 3,
            spaceBetween: 20
          },
          600: {
            slidesPerView: 2,
            spaceBetween: 20
          },
          320: {
            slidesPerView: 1,
            spaceBetween: 20
          }
        }
      }
    }
  }
}
</script>

<style scoped>

  h2 {
    margin-top: 0;
    margin-bottom: 0;
    text-align: left;
    font-size:30px
  }
  .swiper {
    margin-bottom: 2rem;
    cursor: pointer;
  }

  .movie-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 25px 10px;
  }
  
  .poster {
    overflow: auto;
    border-radius: 20px;
    filter: drop-shadow(5px 5px 5px rgb(68, 68, 68));
    transition: all 0.3s ease-in-out;
    width: 100%;
  }

  .movie-item .poster:hover {
    transform:scale(1.1);
  }

  .title {
    font-size:20px;
    color: white;
    text-shadow: 2px 2px 2px gray;
    font-weight: bold;
  }

  .noRating {
    margin: 100px;
    font-size: 30px;
  }
  @media ( max-width: 780px ) {
    h2 {
      margin: 350px 0 0 0;
      font-size: 25px;
    }
  }
  
</style>