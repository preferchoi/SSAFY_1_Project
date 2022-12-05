<template>
  <transition name="modal" appear>
    <div class="modal-overlay" @click.self="$emit('closeBack')">
      <div class="modal-window">
        <div class="update_form">
          <h1>배경 화면 수정</h1>
          <div v-if="myLikeMovies.length !==0" class="update_form_content">
            <div class="back-content">
              <img v-for="movie in myLikeMovies" :key="movie.id"
              :src="`https://www.themoviedb.org/t/p/original${movie?.backdrop_path}`"
              class="backdropImage" 
              :class="{'select-back': movie.id === selected_id }"
              alt=""
              @click="selectBack(movie)"
              >
            </div>
          </div>
          <div v-else class="default-back">
            <h1>배경을 선택하려면 영화에 좋아요❤️를 눌러주세요</h1>
          </div>
          <div class="submit-box">
            <div class="cancel" @click.self="$emit('closeBack')">취소</div>
            <div v-if="myLikeMovies.length !==0" class="submit" @click="vueChangeBackdrop">확인</div>
          </div>
        </div>
      </div>
      
    </div>
  </transition>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: "ProfileBackUpdate",
  props: {
    myLikeMovies: Array
  },
  data() {
    return {
      selected_id: -1,
    }
  },
  computed: {
    ...mapState('Accounts', [
      'username'
    ]),
  },
  methods: {
    ...mapActions('Profile', [
      'changeBackdrop'
    ]),
    selectBack(movie) {
      this.selected_id = movie.id
    },
    vueChangeBackdrop() {
      this.myLikeMovies.forEach((movie)=>{
        if (movie.id === this.selected_id ) {
          console.log(movie.id, this.selected_id)
          this.changeBackdrop({backdrop_path : movie.backdrop_path, username: this.username})
          console.log(movie.backdrop_path)
          this.selected_id = -1
          return false
        } else if (this.selected === -1 ) {
          alert('배경이미지를 선택하세요')
        }
      })
      this.$emit('closeBack')
    }
  },
  created() {
    this.myLikeMovies.forEach((movie)=>{
      movie.selected = false
    })
  }
}
</script>

<style scoped>
  .update_form_content {
    text-align: left;
    width: 100%;
    height: 650px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: auto;
  }
  h1 {
    margin-top:0;
  }
  img:hover {
    filter: brightness(80%); 
  }
  .select-back {
    border: 5px solid black;
    filter: drop-shadow(5px 5px 5px #000);
    height: 185px !important;
    width: 340px !important;
  }
  .backdropImage {
    border-radius: 10px;
    width: 350px;
    margin: 6px;
  }
  form {
    z-index:200;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
  }
  .submit-box {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 30px;
  }
  .modal-window {
    color: black;
    width: 840px;
    height: 820px;
    background-color: rgba(238, 238, 238, 0.877);
    border-radius: 10px;
  }
  .default-back {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 650px
  }
  .back-content {
    text-align:justify
  }

  .submit {
    display: flex;
    justify-content: center;
    align-items: center;
    border: none;
    font-size: 20px;
    width: 70px;
    height: 35px;
    font-weight: bold;
    border-radius: 5px;
    margin: 0 5px;
    background-color: orange;
  }

  .submit:hover {
    background-color: rgba(255, 166, 0, 0.836);
  }

  .cancel {
    font-size: 20px;
    font-weight: bold;
    width: 70px;
    height: 35px;
    border-radius: 5px;
    margin: 0 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(248, 63, 63, 0.8);
  }
  .cancel:hover {
    background-color: rgba(248, 63, 63, 0.692);
  }

  .update_form {
    padding: 5px 10px;
    margin: 15px 20px;
    color: black;
    border-radius: 10px;
    background-color: rgba(238, 238, 238, 0.8);
  }
  .modal-overlay {
    display: flex;
    align-items: center;
    justify-content: center;
    position: fixed;
    z-index: 50;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
  }

 
/* 
트랜지션
*/

  .modal-enter-active{
    transition: opacity 0.4s;
  }

  .modal-leave-active {
    transition: opacity 0.4s;
  }

  .modal-window {
    transition: opacity 0.4s, transform 0.4s;
  }

  .modal-enter, .modal-leave-to {
    opacity: 0;
  }

  /* .modal-window {
    opacity: 0;
    transform: translateY(-20px);
  } */
</style>