<template>
  <div>
    <div class="comment-top">
      <div>
        <h3 style="margin: 0;">{{ comment?.username }}</h3>
      </div>
      <div class='comment-top-btn' v-if="comment.username === username">
        <div class='update-btn' @click="updateActive">수정</div>
        <div class='delete-btn' @click="vueDeleteComment">삭제</div>
      </div>
    </div>

    <div v-if="!update">
      <p style="margin: 5px;">{{ comment?.content }}</p>
    </div>

    <div v-else>
      <form @submit.prevent="vueUpdateComment">
        <input type="text" v-model="content">
        <input type="submit" value="수정">
      </form>
    </div>
    <hr>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: "CommentItem",
  props: {
    comment: Object,
    review: Object,
  },
  data() {
    return {
      update: false,
      content: this.comment.content
    }
  },
  computed: {
    ...mapState('Accounts', [
      'username'
    ])
  },
  methods: {
    ...mapActions('Comments', [
      'updateComment',
      'deleteComment',
    ]),
    updateActive() {
      this.update = !this.update
    },
    vueUpdateComment() {
      this.updateComment({
      commentId: this.comment.id, 
      reviewId: this.review.id, 
      comment: { content : this.content}
      })
      this.update = false
    },
    vueDeleteComment() {
      this.deleteComment({commentId: this.comment.id, reviewId: this.review.id})
    }
  }
}
</script>

<style scoped>
  .comment-top {
    display: flex;
    justify-content: flex-start;
    align-items: center;
  }

  .comment-top-btn {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    margin: 0 5px;
  }

  .update-btn {
    display: flex;
    margin: 0 3px;
    justify-content: center;
    align-items: center;
    font-size: 15px;
    border-radius: 5px;
    color: white;
    background-color: #42b883;
    width: 40px;
  }

  .update-btn:hover {
    background-color: #2e9e6c;
  }

  .delete-btn {
    display: flex;
    margin: 0 3px;
    justify-content: center;
    align-items: center;
    font-size: 15px;
    border-radius: 5px;
    color: white;
    background-color: #f3354e;
    width: 40px;
  }

  .delete-btn:hover {
    background-color: #d12c42;
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