<template>
  <transition name="modal" appear>
    <div class="modal-overlay" @click.self="$emit('close')">
      <div class="modal-window">
        <div class="review-item">
          <div class="review-top">
            <h1><router-link :to="{ name: 'ProfileView', params: { username: review.username} }">{{ review?.username }}</router-link>님의 리뷰</h1>
            <div class="like-box" @click="vueLikeReview">
              <span>
                <i v-if="isReviewLike?.is_review_like" class="fa-solid fa-heart"></i>
                <i v-else class="fa-regular fa-heart"></i>
                &nbsp;{{ isReviewLike?.review_like_count}}</span>
            </div>
          </div>
          <hr>
          <h2>{{ movie?.title }}</h2>
          <star-rating 
          :rating=review.rating 
          :star-size="25" 
          :read-only="true" 
          :show-rating="false"
          :increment="0.01"
          active-color="#d67d24"
          >
          </star-rating>

          <hr>
          <div class="review-content">
            <h2>{{ review?.title }}</h2>
            <p>{{ review?.content }}</p>
            <div class="review-bottom" v-if="review.username === username">
              <div class="update-btn" @click="openUpdate">수정</div>
              <div class="delete-btn" @click="vueDeleteReview" @click.self="$emit('close')">삭제</div>
            </div>
          </div>
          <hr>
        </div>
        <div class="comment-box">
          <CommentList :review="review" :movie="movie"/>
        </div>
        <div class="close-btn" @click.self="$emit('close')">닫기</div>
      </div>
      <UpdateReview @close="closeUpdate" v-if="modal" :movie="movie" :review="review" />
    </div>
    
  </transition>
</template>

<script>
import StarRating from 'vue-star-rating'
import CommentList from '@/components/Review/CommentList'
import UpdateReview from '@/components/Review/UpdateReview'
import { mapActions, mapState } from 'vuex'

export default {
  name: "ReviewModal",
    props: {
      review: Object,
      movie: Object,
    },
    components: {
      StarRating,
      CommentList,
      UpdateReview,
    },
  data() {
    return {
      modal: false,
    }
  },
  methods: {
    ...mapActions('Reviews', [
      'deleteReview',
      'reviewLike',
      'getReviewLike',
    ]),
    ...mapActions('Comments', [
      'getComments'
    ]),
    openUpdate() {
      this.modal = true
    },
    closeUpdate() {
      this.modal = false
    },
    vueDeleteReview() {
      this.deleteReview({movieId: this.movie.id, reviewId: this.review.id})
    },
    vueLikeReview() {
      this.reviewLike(this.review.id)
    }
  },
  computed: {
    ...mapState('Accounts', [
      'username'
    ]),
    ...mapState('Reviews', [
      'isReviewLike'
    ]),
  },
  created() {
    this.getComments(this.review.id)
    this.getReviewLike(this.review.id)
  }
}
</script>

<style scoped>
  .modal-window {
    position: relative;
    color: black;
    width: 700px;
    height: 700px;
    background: #fff;
    border-radius: 10px;
    overflow-y: auto;
  }

  .review-item {
    padding: 5px 20px;
    margin: 15px 20px;
    color: black;
    border-radius: 10px;
    background-color: rgba(238, 238, 238, 0.8);
  }
  
  .review-top {
    display: flex;
    justify-content: flex-start;
    align-items: center;
  }

  .like-box {
    color: white;
    border-radius: 5px;
    margin: 0 15px;
    padding: 3px 10px;
    background-color: rgba(248, 63, 63, 0.8);
  }

  .like-box:hover {
    background-color: rgba(214, 52, 52, 0.8);
  }

  .review-item h1 {
    margin: 5px 0;
  }
  .review-item h2 {
    margin: 5px 0;
  }
  .review-content {
    margin: 0 10px;
    
  }

  .review-item h3 {
    margin: 0;
  }

  .review-item p {
    margin: 0 5px;
  }

  .close-btn {

    font-weight: bold;
    padding: 0;
    margin: 10px auto;
    text-align: center;
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
    width: 70px;
    height: 35px;
    background-color: orange;
  }

  .close-btn:hover {
    background-color: rgba(255, 166, 0, 0.89);
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

  .review-bottom {
    display: flex;
    justify-content: flex-start;
    align-items: center;
  }

  .review-bottom .update-btn {
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    border-radius: 5px;
    margin: 20px 5px 0 0;
    background-color: #42b883;
    width: 60px;
    height: 30px;
  }

  .update-btn:hover {
    background-color: #2e9e6c;
  }

  .review-bottom .delete-btn {
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    border-radius: 5px;
    margin: 20px 0 0 5px;
    background-color: #f3354e;
    width: 60px;
    height: 30px;
  }

  .delete-btn:hover {
    background-color: #d12c42;
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

  a {
    color: #42b883;
  }

  a:hover {
    color: #2e9e6c;
  }


  /* .modal-window {
    opacity: 0;
    transform: translateY(-20px);
  } */
</style>