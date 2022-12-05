<template>
  <transition name="modal" appear>
    <div class="modal-overlay">
      <div class="modal-window">
        <div class="review-item">
          <h1>리뷰수정</h1>
          <hr>
          <h2>{{ movie.title }}</h2>
          <star-rating 
          v-model="rating"
          :star-size="40" 
          :show-rating="false"
          :increment="0.5"
          active-color="#d67d24"
          style="justify-content: center;"
          >
          </star-rating>
          <span style="color:lightgray">별점을 등록해주세요</span>
          <hr>
          <form @submit.prevent="vueUpdateReview">
            <input type="text" v-model="title" placeholder="제목을 입력하세요">
            <input type="textarea" 
            v-model="content" 
            placeholder="내용을 입력하세요, 영화와 상관없는 내용은 약관에 의해 제재를 받을 수 있습니다."
            >
            <div class="submit-box">
              <div class="cancel" @click.self="$emit('close')">취소</div>
              <input type="submit" value="확인">
            </div>
          </form>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import StarRating from 'vue-star-rating'
import { mapActions } from 'vuex'

export default {
  name: "UpdateReview",
  props: {
    movie: Object,
    review: Object,
  },
  components: {
    StarRating,
  },
  data() {
    return {
      title: this.review.title,
      content: this.review.content,
      rating: this.review.rating,
    }
  },
  methods: {
    ...mapActions('Reviews', [
      'updateReview',
    ]),
    vueUpdateReview() {
      if (!this.title) {
        alert('제목을 입력하세요')
      } else if (!this.content) {
        alert('내용을 입력하세요')
      } else if (!this.rating) {
        alert('별점을 등록해주세요')
      }
      else {
        const review = {
          title: this.title,
          content: this.content,
          rating: this.rating,
        }
        this.updateReview({movieId: this.movie.id,
          reviewId: this.review.id,
          review: review})
        this.$emit('close')
      }
    }
  }
}
</script>

<style scoped>
  form {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
  }
  .submit-box {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .modal-window {
    z-index: 50;
    color: black;
    width: 700px;
    background: #fff;
    border-radius: 10px;
  }
  input[type=text] {
    height: 30px;
    width: 85%
  }
  input[type=textarea] {
    height: 300px;
    width: 85%;
    overflow-y: auto;
  }
  input[type=submit] {
    border: none;
    font-size: 20px;
    width: 70px;
    height: 35px;
    font-weight: bold;
    border-radius: 5px;
    margin: 0 5px;
    background-color: orange;
  }

  input[type=submit]:hover {
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

  input {
    margin: 10px 0;
    padding: 5px;
    border-radius: 8px;
    border: none;
    outline: none;
  }
  .review-item {
    padding: 5px 10px;
    margin: 15px 20px;
    color: black;
    border-radius: 10px;
    background-color: rgba(238, 238, 238, 0.8);
  }
  .review-item h1 {
    margin: 5px 0;
  }
  .review-item h2 {
    margin: 5px 0;
  }
  .review-item h3 {
    margin: 0;
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