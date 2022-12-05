<template>
  <div>
    <section class="signup-box">
      <div class="form-box">
        <div>
          <h1>회원 가입</h1>
          <form @submit.prevent="vueSignUp">
            <h3>아이디</h3>
            <input type="text" v-model.trim="username">
            <h3>비밀번호</h3>
            <input type="password" v-model.trim="password">
            <h3>비밀번호 확인</h3>
            <input type="password" v-model.trim="passwordConfirmation"><br>
            <div v-if="message || signUpErrorMessage" class="message-box"><i class="fa-solid fa-circle-exclamation"></i>&nbsp;{{message}}{{ signUpErrorMessage }}</div>
            <input type="submit" value="확인">
            <div></div>
          </form>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'SignUpView',
  data() {
    return{
      username: null,
      password: null,
      passwordConfirmation: null,
      message: null,
    }
  },
  methods: {
    ...mapActions('Accounts', [
      'signUp',
      'delMessage',
    ]),
    vueSignUp() {
      this.message = null
      this.delMessage()

      if (this.password && this.passwordConfirmation && this.username) {
        if (this.password === this.passwordConfirmation) {
          this.message = null
          const credentials = {
            username: this.username,
            password: this.password,
            passwordConfirmation: this.passwordConfirmation,
          }
          this.signUp(credentials)
        } else {
          this.message = '비밀번호가 일치하지 않습니다.'
        }
      } else if (!this.password || !this.passwordConfirmation) {
        this.message = '비밀번호를 입력해주세요'
      } else {
        this.message = '아이디를 입력해주세요'
      }
    }
  },
  computed: {
    ...mapState('Accounts', [
      'signUpErrorMessage'
    ])
  }

}
</script>

<style scoped>
  .signup-box {
    background-image: linear-gradient(135deg, rgba(0,0,0,0) 0%,rgba(0,0,0,0.65) 100%), url("@/assets/login.jpg");
    background-size: 150%, cover !important;
    background-position: 50%, 50% !important;
    height: 100vh;
    padding-top: 10rem;
    display: flex;
  }

  .form-box {
    border-radius: 10px;
    padding: 10px 20px;
    background-color: rgba( 0, 0, 0, 0.9 );
    width: 500px;
    height: 700px;
    margin: 0 auto
  }
  
  h1 {
    font-size: 40px;
  }

  form h3 {
    margin: 15px 45px;
    text-align: start;
  }

  input[type='text'], input[type='password'] {
    text-align: center;
    background-color: rgba(51, 51, 51, 0.9);
    height: 50px;
    border: none;
    border-radius: 5px;
    width: 80%;
    color: white;
    font-size: 20px;
    padding: 0 10px;
  }

  .message-box {
    text-align: center;
    background-color: rgba(187, 220, 88, 0.9);
    height: 50px;
    border: none;
    border-radius: 5px;
    width: 80%;
    color: rgb(0, 0, 0);
    font-size: 15px;
    padding: 0 10px;
    margin: 20px auto;
    display: flex;
    justify-content: flex-start;
    align-items: center;
  }

  input[type=submit] {
    font-size: 25px;
    font-weight: bold;
    color: white;
    border-radius: 10px;
    background-color: #42b883;
    width: 85%;
    height: 50px;
    margin: 20px auto;
  }

  input[type=submit]:hover {
    background-color: #398161;
  } 

  hr {
    background:rgb(226, 226, 226);
    height:1px;
    margin-top:20px;
    opacity: 0.2;
  }
</style>