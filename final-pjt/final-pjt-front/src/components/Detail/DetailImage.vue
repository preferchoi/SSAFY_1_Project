<template>
  <div>
    <div class="image-box">
      <div v-for="image in movieImage?.backdrops.slice(0, 6)" :key="image?.id"> <!--키값 안되면 vote_averge-->
        <img :src="`https://www.themoviedb.org/t/p/original${image?.file_path}`" 
        alt="" 
        class="detail-image"
        @click="open(image?.file_path)"
        >
      </div>
    </div>
    <ImageModal v-if="ImageActivate" :ImageData="ImageData" @close="close()"/>
  </div>
  
</template>

<script>
import ImageModal from '@/components/Detail/ImageModal'
import { mapState } from 'vuex'

export default {
  name: 'DetailImage',
  components: {
    ImageModal,
  },
  computed: {
    ...mapState('MovieDetail', [
      'movieImage',
    ])
  },
  data() {
    return {
      ImageActivate: false,
      ImageData: null,
    }
  },
  methods: {
    open(data) {
      this.ImageData = data
      this.ImageActivate = true
    },
    close() {
      this.ImageData = null
      this.ImageActivate = false
    }
  }
}
</script>

<style scoped>
  h2 {
    margin: 0;
  }

  .image-box {
    display: grid;

    grid-template-columns: 1fr 1fr;
    grid-gap: 10px;
  }
  .detail-image {
    width: 150px;
    border-radius: 10px;
  }

</style>