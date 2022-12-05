<template>
  <div>
    <ProfileIntroduction 
    :profileUsername="username" 
    :myProfile="myProfile"
    :myLikeMovies="myLikeMovies"
    @open="vueUpdateProfile_Open"
    @openBack="vueUpdateProfileBack_Open"
    />
    <!-- <hr class="profile-hr"> -->
    <section class="slider-box">
      <RatingSlider :movies="myRatingMovies"/>
      <LikeSlider :movies="myLikeMovies"/>
    </section>
    <ProfileUpdate 
    v-if="isProfileUpdate" 
    :myProfile="myProfile" 
    :profileUsername="username"
    :myLikeMovies="myLikeMovies" 
    @close="vueUpdateProfile_Close" 
    />
    <ProfileBackUpdate
    v-if="isProfileBackUpdate"
    :myLikeMovies="myLikeMovies"
    @closeBack="vueUpdateProfileBack_Close"
    />
  </div>
</template>

<script>
import ProfileIntroduction from '@/components/Profile/ProfileIntroduction'
import ProfileUpdate from '@/components/Profile/ProfileUpdate'
import ProfileBackUpdate from '@/components/Profile/ProfileBackUpdate'
import LikeSlider from '@/components/Profile/LikeSlider'
import RatingSlider from '@/components/Profile/RatingSlider'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'ProfileView',
  components: {
    ProfileIntroduction,
    ProfileUpdate,
    ProfileBackUpdate,
    RatingSlider,
    LikeSlider,
  },
  data() {
    return {
      username: this.$route.params.username,
      isProfileUpdate: false,
      isProfileBackUpdate: false,
    }
  },
  computed: {
    ...mapState('Profile', [
      'myProfile',
      'myLikeMovies',
      'myRatingMovies',
    ]),
  },
  methods: {
    ...mapActions('Profile', [
      'getMyProfile',
    ]),
    ...mapActions('Accounts', [
        'allPageIn',
        'allPageOut',
    ]),
    vueUpdateProfile_Open() {
      this.isProfileUpdate = true
    },
    vueUpdateProfile_Close() {
      this.isProfileUpdate = false
    },
    vueUpdateProfileBack_Open() {
      this.isProfileBackUpdate = true
    },
    vueUpdateProfileBack_Close() {
      this.isProfileBackUpdate = false
    },
  },
  created() {
    this.allPageIn()
  },
  mounted() {
    this.getMyProfile(this.username)
    setTimeout(() => {
    this.allPageOut()
    }, 1500)
  },
  beforeRouteUpdate(to, from, next) {
    this.username = to.params.username
    this.getMyProfile(this.username)
    next()
  }
}
</script>

<style scoped>
  .slider-box {
    margin: 270px auto;
    width: 70%;
  }

  .profile-hr {
    position: relative;
    top: 250px;
    width: 75%;
    border-radius: 10px;
    background:rgb(226, 226, 226);
    height:1px;
    margin-top:20px;
    opacity: 0.2;

  }

</style>
