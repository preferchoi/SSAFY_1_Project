<template>
  <div>
    <swiper class="carousel" :options="swiperOptions">
      <swiper-slide  
        v-for="movie in movies"
        :key="movie.movieInfo.id">
        <div class="movie-item" :style="{
        background: `linear-gradient(135deg, rgba(0,0,0,0) 0%,rgba(0,0,0,0.65) 100%),
        url('https://www.themoviedb.org/t/p/original${movie?.movieInfo.backdrop_path}')`}">
          <div class="movie-content">
            <div class="movie-content-text">
              <div class = "upBox">
                <div class="upMovie"><p>🏆 이번주 급상승 영화</p></div>
                <router-link :to="{ name: 'DetailView', params: { movieId: movie?.movieInfo.id } }"><div class="upMovie"><p> 더보기 </p></div></router-link>
              </div>
              <h1><span>{{ movie.movieInfo.title }}<br v-if="movie.movieInfo.title.length > 10">&nbsp;({{ movie.movieInfo.original_title }})</span></h1>
              
              <!-- <p>{{ movie.overview }}</p> -->
            </div>
            <iframe
              class="mainVideo"
              :src="`http://www.youtube-nocookie.com/embed/${movie?.movieVideo}`"
              frameborder="0"
              width="800" height="440"
              >
              </iframe>
          </div>
        </div>
      </swiper-slide>
    </swiper>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'

export default {
  name: "Carousel",
  props: {
    movies: Array,
  },
  components : {
    Swiper,
    SwiperSlide,
  },
  data() {
    return {
      swiperOptions: {
        slidesPerView: 1,
        loop: true,
        autoplay: {
          delay: 10000,
        },  
      }
    }
  },
}
</script>

<style scoped>
.movie-item {
  background-size: 150%, cover !important;
  background-position: 50%, 50% !important;
  display: flex;
  justify-content: flex-end;
  height: 100%;
  cursor: move;
}

.carousel {
  margin-top: -6rem !important;
  height: calc(100vh - 5.5rem);
  overflow-x: hidden;
}

.movie-content {
  width: 100%;
  min-height: 480px;
  padding: 20px 50px;
  display: flex;
  justify-content: flex-end;
  align-items: flex-end;
  flex-direction: column;
  margin-bottom: 50px;

}

.movie-content-text {
  text-align: right;
  right: 150px;
  max-width: 700px;
  bottom: 40px;
  margin: 20px;
  min-height: 100px;
  color: white;
}

.movie-content h1 span {
  font-size: 42px;
  font-weight: 500;
  margin-block-start: 0.67em;
  margin-block-end: 0.67em;
  text-shadow: 3px 3px 3px black;
  /* text-decoration: none; */
  color: #fff;
  user-select: none;
}

.movie-content p {
  font-size: 22px;
  font-weight: 200;
  line-height: 26px;
  color: #fff;
  margin-block-start: 1em;
  margin-block-end: 1em;
}

.upMovie p {
  font-weight: 500;
  margin: 0;
}

.upBox {
  display: flex;
  justify-content: right;
  text-align: center;
  margin-bottom: 1rem;
}

.upMovie {
  border-radius: 5px;
  margin: 0 10px;
  width: fit-content;
  padding: 10px 15px;
  background-color: rgba(255, 145, 0, 0.8);
}

.upMovie:hover {
  background-color: rgba(218, 124, 1, 0.8);
}

.mainVideo {
  border-radius: 50px;
}

@media ( max-width: 900px ) {
    .mainVideo {
      width: 100%;
    }
    .movie-content h1 span {
      font-size: 30px;
    }
    .upMovie p {
      font-size: 20px;
    }

    .upMovie {
      padding: 5px 10px;
    }
  }

</style>