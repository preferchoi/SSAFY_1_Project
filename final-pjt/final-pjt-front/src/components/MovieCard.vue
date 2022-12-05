<template>
  <transition name="result" appear>
    <div class="card-box">
      <div class="card">
        <div class="card-content" v-for="movie in searchMovies" :key="movie.id">
          <router-link :to="{ name: 'DetailView', params: { movieId: movie?.id } }">
            <div class="card-item">
              <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movie?.poster_path}`" 
              alt="poster" 
              class='poster'>
              <div class="movieTitle">
                <h3>{{movie.title.substr(0, 15)}}</h3>
              </div>
            </div>
          </router-link>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'MovieCard',
  computed: {
    ...mapState('Movies', [
      'searchMovies'
    ])
  }
}
</script>

<style scoped>

  .card {
    width:95%;
    margin: 0 auto;
    display: flex;
    flex-wrap: wrap;
  }

  .card-content { 
    color: black;
    border-radius: 10px;
    margin: 20px 20px;
  }

  h3 {
    margin: 10px 0;
    text-shadow: 5px 5px 5px gray;
  }

  img {
    width: 250px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
  }
  
  .card-item {
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 10px;
    filter: drop-shadow(5px 5px 5px rgb(68, 68, 68));
    transition: all 0.3s ease-in-out;

    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .card-item:hover {
    transform:scale(1.05);
  }
  
  .result-enter-active{
    transition: opacity 0.8s;
  }

  .result-leave-active {
    transition: opacity 0.4s;
  }

  .result-enter, .result-leave-to {
    opacity: 0;
  }

  a {
    text-decoration: none;
    color: black
  }

  @media ( max-width: 800px ) {
  .card  {
      justify-content: center;
    }
  }
</style>