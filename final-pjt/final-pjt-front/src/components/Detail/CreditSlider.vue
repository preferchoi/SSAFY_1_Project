<template>
  <section>
    <h2>{{ title }}</h2>
    <swiper class="swiper" :options="swiperOptions">
      <swiper-slide
        v-for="people in movieCredit?.cast"
        :key="`${people?.id}${people?.character}`">
        <div class="movie-item">
          <img v-if="people?.profile_path" :src="`https://www.themoviedb.org/t/p/original${people?.profile_path}`" alt="" class="poster">
          <img v-else src="@/assets/Unknown.jpg" alt="">
          <span>
            <p>{{ people?.name }}</p>
            <p style="font-size:14px; color:gray">{{ people?.character.substr(0, 15) }} 역</p>
          </span>
        </div>
      </swiper-slide>
    </swiper>
  </section>
</template>

<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'

export default {
  name: "CreditSlider",
  props: {
    movieCredit: Object,
    title: String,
  },
  components : {
    Swiper,
    SwiperSlide
  },
  data() {
    return {      
      swiperOptions: {
        // mousewheel: true,
        spaceBetween: 10,
        // autoplay: {
        //   delay: 2500,
        //   disableOnInteraction: false
        // },
        loop: true,
        loopFillGroupWithBlank: true,
        breakpoints: {
          1060: {
            slidesPerView: 6,
            spaceBetween: 20
          },
          800: {
            slidesPerView: 5,
            spaceBetween: 20
          },
          630: {
            slidesPerView: 4,
            spaceBetween: 20
          },
          320: {
            slidesPerView: 3,
            spaceBetween: 20
          }
        }
      }
    }
  }
}
</script>

<style scoped>

  section h2 {
    margin-left: 2rem;
    text-align: left;
    font-weight: bold;
  }

  .swiper {
    margin: 0 2rem;
    cursor: pointer;
  }

  .movie-item {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .poster {
    filter: drop-shadow(5px 5px 5px rgb(68, 68, 68));
    transition: all 0.3s ease-in-out;

  }

  img {
    border-radius: 10px;
    object-fit: cover;
    max-height: 200px;
    width: 100%
  }

  div p {
    margin: 2px 0;
  }

</style>