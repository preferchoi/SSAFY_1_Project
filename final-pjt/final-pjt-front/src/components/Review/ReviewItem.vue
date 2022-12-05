<template>
  <div>
    <div class="review-item" @click="openModal">
      <star-rating 
        :rating=review.rating 
        :star-size="18" 
        :read-only="true" 
        :show-rating="false"
        :increment="0.01"
        active-color="#d67d24"
        >
        </star-rating>
      <div class="review-content">
        <h3>{{ review?.username }} :&nbsp;<span>{{ review?.title }}</span></h3>
        <p>{{ review?.content }}</p>
      </div>
    </div>
    <ReviewModal @close="closeModal" v-if="modal" :movie="movie" :review="review" />
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
import ReviewModal from '@/components/Review/ReviewModal.vue'
import { mapActions } from 'vuex'

export default {
  name: 'ReviewItem',
  components: {
    StarRating,
    ReviewModal,
  },
  props: {
    review: Object,
    movie: Object,
  },
  data() {
    return {
      modal: false,
    }
  },
  methods: {
    ...mapActions('Comments', [
      'getComments'
    ]),
    openModal() {
      this.modal = true
    },
    closeModal() {
      this.modal = false
    },
  },
  created() {
    this.getComments(this.review.id)
  }
}
</script>

<style scoped>

  .review-item {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    padding: 5px 10px;
    margin: 15px 0;
    color: black;
    border-radius: 10px;
    background-color: rgba(255, 255, 255, 0.8);
  }

  .review-content {
    margin: 0 10px;
    height: 50px;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .review-item h3 {
    margin: 0;
  }

  .review-item p {
    margin: 0 5px;
  }
</style>