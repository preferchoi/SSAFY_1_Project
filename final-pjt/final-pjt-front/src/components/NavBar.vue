<template>
  <header>
    <div class="nav-left">
      <router-link :to="{ name: 'HomeView'}">
        <span class="navlogo"><img src="@/assets/logo.png" alt=""><h2 class="logo">uepago</h2></span>
      </router-link>
      <router-link :to="{ name: 'RecommendationView'}">
        <h2>추천 영화</h2>
      </router-link>
    </div>
    <div class="nav-right">
      <router-link :to="{ name: 'SearchView' }">
        <div class="search-btn">
          <i class="fas fa-search"></i>
        </div>
      </router-link>
      <router-link v-if="!token" :to="{ name: 'SignUpView'}">
        <h2>회원 가입</h2>
      </router-link>
      <router-link v-if="!token" :to="{ name: 'LogInView'}">
        <h2>로그인</h2>
      </router-link>
      <router-link  class="navUser" v-if="token" :to="{ name: 'ProfileView', params: { username: username} }">
        <img class=navProfileImage :src="profileImage" alt="">
        <h2>{{ username }} 님</h2>
      </router-link>
      <div v-if="isLoggedIn">
        <h2 @click="vueLogOut">로그아웃</h2>
      </div>
    </div>
  </header>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'

export default {
  name: 'NavBar',
  data() {
    return {
      profileSrc: require('@/assets/Unknown-profile.jpg'),
    }
  },
  computed: {
    ...mapState('Accounts', [
      'token',
      'username',
    ]),
    ...mapState('Profile', [
      'navProfile'
    ]),
    ...mapGetters('Accounts', [
      'isLoggedIn'
    ]),
    profileImage() {
      if (this.navProfile?.img_path) {
        console.log(this.navProfile?.img_path)
        return `http://127.0.0.1:8000${this.navProfile?.img_path}`
      } else {
        return this.profileSrc
      }
    }
  },
  methods: {
    ...mapActions('Accounts', [
      'logOut'
    ]),
    vueLogOut() {
      this.logOut()
    }
  }
};

</script>

<style scoped>
  header {
    position: fixed;
    z-index: 100;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 20px 30px;
    background-color: #1f1f1f;
    height: 2rem;
    top: 0;
    right: 0;
    left: 0;
    transition: all 0.5s;
  }

  .logo {
    font-size: 37px;
    font-family: 'Yanone Kaffeesatz', sans-serif;
  }

  .navlogo {
    display: flex;
    justify-content: center;
    align-items: center;

    
  }

  .navlogo:hover h2 {
    color:gray;
  }

  .navlogo img {
    width: 35px;
    margin-bottom: 5px;;
  }

  .nav-left {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .nav-right {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .header_dark {
    background-color: #1f1f1f;
  }

  header h2 {
    color: #fff;
  }
  .search-btn {
    color: white;
    /* color: #42b883; */
    font-size: 24px;
    padding-right: 20px;
  }
  .search-btn:hover {
    color: #42b883;
  }

  header h2:hover {
    color: gray
  }

  a {
    padding: 0 10px;
    margin: 0 10px;
  }
  a.router-link-exact-active h2{
  color: #42b983;
  }

  a.router-link-exact-active .search-btn{
  color: #42b983;
  }

  .navProfileImage {
    object-fit: cover;
    width: 55px;
    height: 55px;
    border-radius: 100px;
    margin: 0 10px;
  }

  .navUser {
    display: flex;
    justify-content: center;
    align-items: center;
  }


  @media ( max-width: 800px ) {
    h2 {
      font-size: 20px
    }
  }

  @media ( max-width: 720px ) {
    h2 {
      font-size: 16px;
    }
    .logo {
      font-size: 0;
    }
    
    a {
      margin: 0;
    }
  }

</style>