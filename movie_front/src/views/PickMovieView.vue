<template>
  <div class="p-5">
    <h1 class="mb-5">Pick Movie</h1>
    <div class="container">       
      <PickItem :movies="movies"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import PickItem from '@/components/pickmovies/PickItem.vue'

const MOIVE_API_URL = 'http://127.0.0.1:8000/movies/'
export default {
  name: 'PickMovieView',
  data() {
    return {
      movies: [],
    }
  },
  components: {
      PickItem,
  },
  methods: {
    getMovie() {
      axios.get(MOIVE_API_URL)
      .then(res => {
        this.movies = res.data
        console.log(this.movies)
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  mounted() {
    this.getMovie()
  },
}
</script>

<style>

</style>