<template>
  <transition name="modal" appear>
    <div class="modal-overlay" @click.self="$emit('close')">
      <div class="modal-window">
        <div class="update_form">
          <h1>프로필 사진 수정</h1>
          <form @submit.prevent="vueUpdateProfile">
            <div class="filebox">
              <input class="upload-name" :value="file_name" :placeholder="file_name">
              <label for="file">파일찾기</label> 
              <input @change="fileChange" type="file" accept="image/*" id="file">
            </div>
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

import { mapActions, mapState } from 'vuex'

export default {
  name: "ProfileUpdate",
  props: {
    profileUsername: String,
    myProfile: Object,
    myLikeMovies: Array,
  },
  data() {
    return {
      file_name: "파일을 선택하세요.",
      message: "Hello, world", 
      file: "", 
      mg_src: "",
    }
  },
  computed: {
    ...mapState('Profile', [
      'user_pk'
    ])
  },
  methods: {
    ...mapActions('Profile', [
      'updateProfile',
    ]),
    vueUpdateProfile() {
      if (!this.file) {
        alert('이미지를 업로드해주세요.')
      } else {
        const form = new FormData()
        form.append("img_path", this.file)
        this.updateProfile({form: form, username: this.profileUsername})
        this.$emit('close')
      }
    },
    fileChange: function(e) {
      console.log(e.target.files)
      this.file = e.target.files[0]
      this.file_name = e.target.files[0].name
      console.log(this.file)
    },
    profileSubmit() {
      if (!this.file) {
        this.file_name
      }
    }  
  }
}
</script>

<style scoped>
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
    width: 700px;
    background-color: rgba(238, 238, 238, 0.877);
    border-radius: 10px;
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

  .filebox {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .filebox .upload-name { 
    height: 40px;
    padding: 0 10px;
    border: 1px solid #dddddd;
    width: 100%;
    color: #999999;
  }

  .filebox label {
    width: 100px;
    border-radius: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
    background-color: #999999;
    cursor: pointer;
    height: 40px;
    margin-left: 10px;
  }

  .filebox input[type="file"] {
    position: absolute;
    width: 0;
    height: 0;
    padding: 0;
    overflow: hidden;
    border: 0;
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