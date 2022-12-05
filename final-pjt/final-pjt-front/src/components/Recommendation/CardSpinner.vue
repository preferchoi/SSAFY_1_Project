<template>
  <transition name="modal" appear>
    <div class="modal-overlay" @click.self="$emit('close')">
      <div class="modal-window" @click.self="$emit('close')">
        <div class="modal-content" @click.self="$emit('close')">
          <h1 style="text-align:center;">카드를 뒤집어 보세요</h1>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>

export default {
  name: "CardSpinner",
  components: {
  },
}
</script>

<style scoped>
  .modal-window {
    display: flex;
    justify-content: center;
    align-items: center;
    color: black;
    width: fit-content;
    height: fit-content;
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
    background: rgba(0, 0, 0, 0.8);
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