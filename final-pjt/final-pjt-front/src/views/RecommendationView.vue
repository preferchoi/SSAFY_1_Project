<template>
  <div>

    <div class="btn-box">
        <div class="btn">
          <div class="btn-content">
            <img src="@/assets/logo.png" alt="">
            <h1 class="logo">uepago</h1>
          </div>
          <div class="btn-content">
            <img src="@/assets/button.png" alt=""  @click="vueDoAnalysis">
            <h3>&nbsp;버튼을 눌러 알고리즘을 실행하세요</h3>
          </div>
        </div>
    </div>
    <div v-if="myRecommendation.length !== 0" class="card_box">
      <div v-for="(movie, index) in myRecommendation" :key="movie.id" class="card" @click="flip(index)" :class="{'backRotate': !card_flip[index], 'cardRotate': card_flip[index]}" >
        <div class="front"><img src="@/assets/card_back.png" alt="" class="card_back"></div>
        <div class="back">
          <router-link :to="{ name: 'DetailView', params: { movieId: movie?.id } }">
            <img :src="`https://www.themoviedb.org/t/p/original${movie?.poster_path}`" alt=""><h1>{{movie?.title}}</h1>
          </router-link>
        </div>
      </div>
    </div>

    <div v-else class="card_box">
      <div v-for="index in 3" :key="`default${index}`" class="card backRotate">
        {{index}}
        <div class="front"><img src="@/assets/card_back.png" alt="" class="card_back"></div>
      </div>
    </div>
    <CardSpinner v-if="carding" @close="close_carding"/>
    <Spinner v-if="isLoading"/>
    
  </div>
</template>

<script>
import Spinner from '@/components/Recommendation/Spinner'
import CardSpinner from '@/components/Recommendation/CardSpinner'

import { mapActions, mapState } from 'vuex'

export default {
  name: 'RecommendationView',
  components: {
    Spinner,
    CardSpinner
  },
  computed: {
    ...mapState('Profile', [
      'my_pk',
    ]),
    ...mapState('Recommendation', [
      'myRecommendation',
      'isLoading',
    ]),
    ...mapState('Profile', [
      'myLikeMovies'
    ])
  },
  data() {
    return {
      card_flip: {
      0: false,
      1: false,
      2: false,
      },
      carding: false
    }
  },
  methods: {
    ...mapActions('Recommendation', [
      'doAnalysis',
      'getMyLikeMovies'
    ]),
    vueDoAnalysis() {
      console.log(1)
      console.log(this.myLikeMovies)
      console.log(this.myLikeMovies?.length)
      if (this.myLikeMovies?.length < 5) {
        console.log(this.myLikeMovies.length)
        console.log(111)

        alert('❤️ 좋아요를 누른 영화가 5개 이상 필요합니다.')
        this.$router.push({ name: "HomeView"})
      } else {
        this.doAnalysis(this.my_pk)
        this.carding = true
      }
      for (let i=0; i < 3; i++) {
        this.card_flip[i] = false
      }
    },
    flip(index) {
      this.card_flip[index] = true
    },
    close_carding() {
      this.carding = false
    }
  },
  created() {
    this.getMyLikeMovies(this.my_pk)
    console.log(this.myLikeMovies)
    if (this.myRecommendation?.length !==0) {
      for (let i=0; i < 3; i++) {
        this.card_flip[i] = true
      }
    }
  },
}
</script>

<style scoped>
  .btn-box {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .btn {
    font-size: 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    width: 600px;
    height: 150px;
    margin-top:45px;
    border-radius: 40px;
  }

  .btn-content {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .btn img {
    width: 100px;
    margin-bottom: 10px;
  }

  .btn h1 {
    font-size: 100px;
    margin-top: 10px;
    margin-bottom: 0;
    font-family: 'Yanone Kaffeesatz', sans-serif;
  }

 .btn h3 {
  color: gray;
 }

  .card_box img:hover {
    transform:scale(1.1);
  }

  .btn-content img:hover {
    transform:scale(0.9);
  }

  img {
    transition: all 0.3s ease-in-out;
  }

  a {
    text-decoration: none;
    color: white
  }

  .btn-content:hover {
    color: #42b983;
  }

  .card_box {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
  }

  .card {
    width: 450px;
    height: 600px;
    position:relative; 
    display:inline-block;
    margin: 100px 15px;
    filter: drop-shadow(10px 10px 10px rgb(255, 255, 255));
  }

  .card img {
    border-radius: 40px;
    height: 500px;
  }

  .card_back {
    filter: brightness(0.8);
  }

  .front { 
    position:absolute; 
    /* width:100px; 
    height:150px;  */
    top:0; left:0;
  }

  .back { 
    position:absolute; 
    display: flex;
    flex-direction: column;
    /* width:100px; 
    height:150px;  */
    top:0; 
    left:0; 
    transform:rotateY(90deg);
  }

  .cardRotate .front { 
    opacity:1;
    animation: rotateAni 0.5s 1; 
    transform:rotateY(90deg);
  }
  .cardRotate .back { 
    opacity:1;animation: rotateAni2 0.5s 0.5s 1 backwards; 
    transform:rotateY(0);
  }
  .backRotate .front{
    animation: backAni 0.5s 1; 
    opacity:1;
  }
  .backRotate .back { 
    opacity:0;
  }

  @keyframes rotateAni{
    0%{transform:rotateY(0);}
    100%{transform:rotateY(90deg);}
  }

  @keyframes rotateAni2{
    0%{transform:rotateY(-90deg);}
    100%{transform:rotateY(0deg);}
  }

  @keyframes backAni{
    0%{transform:rotateY(90deg);}
    100%{transform:rotateY(0deg);}
}

</style>