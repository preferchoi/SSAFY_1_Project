<template>
  <div class="profile-main">
    <div class="profile-background" :style="{
      background: 
      `linear-gradient(135deg, rgba(0,0,0,0) 0%,rgba(0,0,0,0.0) 100%),
      url('${backdropImage}')`}">
      <div class="profile-box">
        <div class="profile-back">
          <div class="profile-image"
          :style="{background: `url('${profileImage}')`}"
          >
          </div>
          <!-- <i class="fa-solid fa-plus fa-4x profile-update-plus-btn"></i> -->
        </div>
        <div class="profile-content">
          <h1>{{ profileUsername }}</h1>  
          <div class="follow-content">
            <div>팔로워 {{ followData?.follower_count }} 명&nbsp;•</div>&nbsp;
            <div>팔로잉 {{ followData?.following_count }} 명</div>
            <div v-if="profileUsername !== username">
              <div v-if="!followData?.is_following" 
              class="follow-btn" 
              @click="vueFollow">팔로잉</div>
              <div v-else class="unfollow-btn" @click="vueFollow">언팔로우</div>
            </div>
          </div>
          <!-- <div v-if="profileUsername === username" class="profile-update-btn" 
            @click.self="$emit('open')">프로필수정
          </div> -->
          <v-dropdown
          v-if="profileUsername === username"
          class="profile-update-btn"
          :noPadding="true"
          :zIndex="0"
          >
          <div>프로필 수정</div>
          <template #portal>
            <div class="drop item1" @click.self="$emit('open')">프로필 사진 수정</div>
            <div class="drop item2" @click.self="$emit('openBack')">배경 화면 수정</div>
          </template>
        </v-dropdown>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex' 

export default {
  name: 'ProfileIntroduction',
  props: {
    profileUsername: String,
    myProfile: Object,
    myLikeMovies: Array,
  },
  data() {
    return {
      bgSrc: require('@/assets/profile_back_default.jpg'),
      profileSrc: require('@/assets/Unknown-profile.jpg'),
      isProfileUpdate: false,
    }
  },
  computed: {
    ...mapState('Profile', [
      'user_pk',
      'followData',
    ]),
    ...mapState('Accounts', [
      'username',
    ]),
    profileImage() {
      if (this.myProfile?.img_path) {
        return `http://127.0.0.1:8000${this.myProfile?.img_path}`
      } else {
        return this.profileSrc
      }
    },
    backdropImage() {
      if (this.myProfile?.backdrop_path) {
        return `https://www.themoviedb.org/t/p/original${this.myProfile?.backdrop_path}`
      } else {
        return this.bgSrc
      }
    }
  },
  methods: {
    ...mapActions('Profile', [
      'doFollow',
      ]),
    vueFollow() {
      this.doFollow(this.user_pk)
    },
  }
}
</script>

<style>
  .profile-main {
    margin-top: 70px;
  }

  .profile-background {
    background-size: 150%, cover !important;
    background-position: 50%, 50% !important;
    background-repeat:no-repeat;
    position: relative;
    width: 100%;
    height: 700px;
  }

  .profile-box {
    display: flex;
    justify-content: flex-start;
    position: absolute;
    margin-left: 20%;
    height: fit-content;
    top:550px;
  }

  .profile-content {
    text-align: start;
    margin: 140px 30px;
    width: fit-content
  }

  .profile-content h1{
    font-size: 40px;
    margin-bottom: 10px;
  }


  .follow-content {
    color:rgb(160, 160, 160);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .profile-back {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #1f1f1f;
    border-radius: 400px;
    width: 300px !important; 
    height: 300px !important;
    padding: 10px;
  }

  .profile-image {
    width: 100%;
    height: 100%;
    border-radius: 400px;
    background-color: red;
    background-size: cover !important;
    background-position: 50%, 50% !important;
    background-repeat:no-repeat;
  }

  .unfollow-btn{
    font-weight: bold;
    color: white;
    padding: 5px 10px;
    margin-left: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    width: fit-content;
    border: 3px solid #42b883;
    background-color: #42b883;
    border-radius: 50px;
  }

  .unfollow-btn:hover{
    background-color: #2e9e6c;
    border: 3px solid #2e9e6c;
  }

  .follow-btn {
    font-weight: bold;
    color: white;
    padding: 5px 10px;
    margin-left: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    width: fit-content;
    border: 3px solid #42b883;
    border-radius: 50px;
  }

  .follow-btn:hover{
    background-color: #42b883;
  }

  .profile-update-btn {
    font-size: 18px;
    font-weight: bold;
    color: white;
    padding: 8px 16px;
    margin-top: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    width: fit-content;
    background-color: rgba(97, 97, 97, 0.5);
    border-radius: 20px;
  }

  .profile-update-btn:hover {
    background-color: rgba(97, 97, 97, 0.9);
  }

  .drop {
    padding: 10px;
  }
  
  .item1:hover, .item2:hover {
    background-color: lightgray;
  }

  @media ( max-width: 780px ) {
    .profile-box {
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 0;
    }
    .profile-content {
      text-align: center;
      margin: auto;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      
    }
    h1 {
      margin: 0
    }
    .profile-update-btn {
      margin: auto
    }
    .follow-content {
      margin-bottom: 10px
    }
  }


</style>