<template>
  <div>
    <div class="review-box">
      <div class="review-top">
        <h1>영화 리뷰 &nbsp;<i @click="reviewMoreClick" class="fa-solid fa-plus"></i></h1>
        <div class="create-review" @click="openReviewForm">리뷰 작성</div>
      </div>
      <div v-if="!reviewMore">
        <ReviewItem v-for="review in reviews.slice(0,3)" :key="review.id" :movie="movie" :review="review"/>
      </div>
      <div v-else>
        <ReviewItem v-for="review in reviews" :key="review.id" :movie="movie" :review="review"/>
      </div>
    </div>
    <CreateReview @close="closeReviewForm" v-if="reviewFormActive" :movie="movie"/>
  </div>
</template>

<script>
import ReviewItem from '@/components/Review/ReviewItem'
import CreateReview from '@/components/Review/CreateReview'
import { mapState } from 'vuex'

export default {
  name: 'ReviewList',
  props: {
    movie: Object
  },
  components: {
    ReviewItem,
    CreateReview,
  },
  data() {
    return {
      reviewMore: false,
      reviewFormActive: false,
    }
  },
  computed: {
    ...mapState('Reviews', [
      'reviews',
    ])
  },
  methods: {
    reviewMoreClick() {
      this.reviewMore = !this.reviewMore
    },
    openReviewForm () {
      this.reviewFormActive = true
    },
    closeReviewForm () {
      this.reviewFormActive = false
    },
    clickCallback(pageNum) {
      console.log(pageNum)
    }
  }
}
</script>

<style scoped>
  .review-box {
    margin: 0 20px;
    text-align: left;
  }

  .create-review {
    border-radius: 5px;
    margin: 5px 15px;
    color: black;
    font-weight: bold;
    padding: 3px 10px;
    background-color: rgba(255, 196, 0, 0.8);
  }
  .review-top {
    display: flex;
    justify-content: flex-start;
    align-items: baseline;
  }
</style>