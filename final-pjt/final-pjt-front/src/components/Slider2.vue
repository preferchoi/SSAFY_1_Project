<template>
  <section>
    <h2>{{ title }}</h2>
    <swiper class="swiper" :options="swiperOptions">
      <swiper-slide
        v-for="movie in movies"
        :key="movie?.id">
        <div class="movie-item">
          <router-link :to="{ name: 'DetailView', params: { movieId: movie?.id } }">
          <img :src="posterSrc(movie)" alt="" class="poster">
          <span class="title">{{ movie?.title }}</span>    
          </router-link>
        </div>
      </swiper-slide>
    </swiper>
  </section>
</template>

<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'

export default {
  name: "Slider2",
  props: {
    movies: Array,
    title: String,
  },
  components : {
    Swiper,
    SwiperSlide
  },
  methods: {
    posterSrc(movie) {
      if (movie?.poster_path) {
        return `https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movie?.poster_path}`
      } else {
        return require('@/assets/movie404.png')
      }
    }
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
        loop: true,
        loopFillGroupWithBlank: true,
        breakpoints: {
          1500: {
            slidesPerView: 7,
            spaceBetween: 20
          },
          1280: {
            slidesPerView: 6,
            spaceBetween: 20
          },
          1060: {
            slidesPerView: 5,
            spaceBetween: 20
          },
          800: {
            slidesPerView: 4,
            spaceBetween: 20
          },
          530: {
            slidesPerView: 3,
            spaceBetween: 20
          },
          320: {
            slidesPerView: 2,
            spaceBetween: 20
          }
        }
      }
    }
  }
}
</script>

<style scoped>
  section {
    margin: 0 20px;
  }
  h2 {
    margin-top: 1rem;
    margin-bottom: 0;
    text-align: left;
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
    color: white;

  }
  
</style>