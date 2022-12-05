<template>
  <div>
    <section class="login-box">
      <div class="form-box">
        <div>
          <h1>로그인</h1>
          <form @submit.prevent="vueLogin">
            <h3>아이디</h3>
            <input type="text" v-model.trim="username">
            <h3>비밀번호</h3>
            <input type="password" v-model.trim="password">
            <div v-if="logInErrorMessage" class="message-box"><i class="fa-solid fa-circle-exclamation"></i>&nbsp;{{ logInErrorMessage }}</div>
            <input type="submit" value="확인">
          </form>
          <p style="color:gray">회원이 아니신가요?&nbsp; <span style="color:white" @click="goSignUp">지금 가입하세요</span></p>
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
    }
  },
  computed: {
    ...mapState('Accounts', [
      'logInErrorMessage'
    ])
  },
  methods: {
    ...mapActions('Accounts', [
      'logIn'
    ]),
    vueLogin() {
      const credential = {
        username: this.username,
        password: this.password,
      }
      this.logIn(credential)
    },
    goSignUp() {
      this.$router.push({name: 'SignUpView'})
    }
  }

}
</script>

<style scoped>
  .login-box {
    background-image: linear-gradient(135deg, rgba(0,0,0,0) 0%,rgba(0,0,0,0.65) 100%), url("@/assets/login.jpg");
    background-size: 150%, cover !important;
    background-position: 50%, 50% !important;
    height: 100vh;
    padding-top: 10rem;
    display: flex;
  }
  
  .message-box {
    text-align: center;
    background-color: rgba(187, 220, 88, 0.9);
    height: 50px;
    border: none;
    border-radius: 5px;
    width: 80%;
    color: rgb(133, 63, 63);
    font-size: 15px;
    padding: 0 10px;
    margin: 20px auto;
    display: flex;
    justify-content: flex-start;
    align-items: center;
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

  p span:hover {
    text-decoration : underline
  }
</style>