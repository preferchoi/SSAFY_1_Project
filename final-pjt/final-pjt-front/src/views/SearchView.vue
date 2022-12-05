<template>
  <div class="search">
    <form @submit.prevent="searching" class="search-box">
      <input
        type="text"
        placeholder="영화 제목을 입력해주세요"
        :value="search"
        @keyup="searching"
      />
    <input type="submit" value="검색" />
    </form>
    <h1>{{ search }} 검색 결과</h1>
    <MovieCard/>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import { mapActions, mapState } from 'vuex'

export default {
  name: "SearchView",
  data() {
    return {
      search: '',
    }
  },
  computed: {
    ...mapState('Movies', [
      'searchMovies'
    ])
  },
  methods: {
    ...mapActions('Movies', [
      'getSearchMovies'
    ]),
    searching(e) {
      this.search = e.target.value
      if (this.search) {
        this.getSearchMovies(this.search)
      }
    }
  },
  components: {
    MovieCard,
  }
}
</script>

<style scoped>
  .search {
    margin: 100px auto;
    padding: 0 20px 20px 20px;
    color: #fff;
  }
  .search-box {
    margin: auto;
    max-width: 1000px;
    height: 100px;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
  }
  .search-box input {
    border: none;
    outline: none;
  }

  .search-box input[type="text"] {
    width: 100%;
    height: 40px;
    color: black;
    background-color: rgba(255, 255, 255, 0.9);
    font-size: 20px;
    padding: 10px 16px;
    border-radius: 8px;
    transition: 0.4s;
  }

  .search-box input[type="submit"] {
    width: 120px;
    height: 60px;
    background-color: #42b883;
    color: #fff;
    border: 0;
    border-top-right-radius: 8px;
    border-bottom-right-radius: 8px;
    cursor: pointer;
    font-weight: bold;
    font-size: 30px;
    position: absolute;
    right: 0;
  }
  .search-box input:active {
    background-color: #3b8070;
    color: white;
  }

  .search-box input:active::placeholder{
    color: white;
  }

</style>