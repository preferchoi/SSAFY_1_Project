<template>
  <transition name="modal" appear>
    <div class="modal-overlay" @click.self="$emit('close')">
      <div class="modal-window">
        <img :src="`https://www.themoviedb.org/t/p/original${ImageData}`" alt="">
      </div>
    </div>
  </transition>
</template>

<script>


export default {
  name: "ImageModal",
  props: {
    ImageData: String,
  },
}
</script>

<style scoped>

  .modal-window {
    color: black;
    width: fit-content;
    height: 360px;
    background-color: rgba(238, 238, 238, 0.877);
    border-radius: 10px;
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

  img {
    width: 700px;
    border-radius:10px
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