<template>
  <footer>
    <div class="foot">
      Copyright 2022. 
      <a href="https://github.com/tayo5712" target="_blank"><i class="fa-brands fa-github"></i> Tayo</a> , 
      <a href="https://github.com/preferchoi" target="_blank"><i class="fa-brands fa-github"></i> Prefer_Choi</a> All rights reserved.
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style scoped>
  footer {
    position:absolute;                         
    display: flex;
    bottom:0;
    left: 0;
    right: 0;
    justify-content: center;
    align-items: center;
    padding: 10px 20px;
    background-color: #1f1f1f;
    height: 1rem
  }

  a {
    text-decoration: none;
    color: gray;
  }

  .foot {
    color: gray;
    opacity: 0.4;
  }


</style>