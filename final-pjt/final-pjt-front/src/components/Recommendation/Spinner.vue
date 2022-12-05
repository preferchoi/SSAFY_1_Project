<template>
  <transition name="modal" appear>
    <div class="modal-overlay">
      <div class="modal-window">
        <div class="modal-content">
          <h1 style="text-align:center;">분석중 ...</h1>
          <pulse-loader size="60px" margin="10px"></pulse-loader>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'

export default {
  name: "Spinner",
  components: {
    PulseLoader
  },
}
</script>

<style scoped>
  .modal-window {
    display: flex;
    justify-content: center;
    align-items: center;
    color: black;
    width: 400px;
    height: 200px;
    background-color: rgba(51, 51, 51, 1);
    border-radius: 10px;
  }
  .modal-overlay {
    display: flex;
    align-items: center;
    justify-content: center;
    position: fixed;
    z-index: 500;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
  }
  .modal-content {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }

  .modal-content h1 {
    color: white
  }

 
/* 
트랜지션
*/

  /* .modal-enter-active{
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
  } */

  /* .modal-window {
    opacity: 0;
    transform: translateY(-20px);
  } */
</style>