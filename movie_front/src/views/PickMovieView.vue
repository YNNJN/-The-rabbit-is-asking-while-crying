<template>
  <div class="p-5">
    <h1>Pick Movie</h1>
    <div class="container">       
        <PickItem/>
    </div>
  </div>
</template>

<script>
import PickItem from '@/components/PickItem.vue'

export default {
  name: 'PickMovieView',
  components: {
      PickItem,
  },
}
</script>

<style>

</style>