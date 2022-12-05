<template>
  <div>
    <div class="comment-box">
      <h1>댓글</h1>
      <div style="margin: 0 10px;">
        <form @submit.prevent="vueCreateComment">
          <input type="text" v-model="content">
          <input type="submit">
        </form>
        <hr>
        <CommentItem v-for="comment in comments" 
        :key="comment.id" 
        :comment="comment" 
        :review="review"/>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import CommentItem from '@/components/Review/CommentItem'

export default {
  name: "CommentList",
  props: {
    review: Object,
    movie: Object,
  },
  components: {
    CommentItem
  },
  data() {
    return {
      content: null,
    }
  },
  computed: {
    ...mapState('Comments', [
      'comments'
    ])
  },
  methods: {
    ...mapActions('Comments', [
      'createComment'
    ]),
    vueCreateComment() {
      this.createComment({reviewId: this.review.id, comment: {content: this.content}})
      this.content = null
    }
  },
}
</script>

<style scoped>
  .comment-box {
    padding: 5px 10px;
    margin: 15px 20px;
    color: black;
    border-radius: 10px;
    background-color: rgba(238, 238, 238, 0.8);
  }

  .comment-box h1 {
    margin: 10px 20px;
  }

  form {
    display: flex;
    justify-content: flex-start;
    align-items: center;
  }

  input[type=text] {
    height: 30px;
    width: 85%
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
    background-color: rgba(255, 166, 0, 0.89);
  }

  input {
    padding: 5px;
    border-radius: 8px;
    border: none;
    outline: none;
  }

</style>