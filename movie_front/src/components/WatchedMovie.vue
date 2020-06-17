<template>
  <div class="container text-center">
    <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
        <div class="carousel-inner w-50">
            <div v-for="movie in movies" :key="movie.DOCID" class="carousel-item active">
                <img :src="movie.posters" class="d-block w-100" :alt="movie.title">
            </div>
        </div>
        <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
        </a>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000/'

export default {
  name: 'WatchedMovie',
  data() {
      return {
          movies: [],
      }      
  },
  props: {
      user_info: {
          type: Object,
      }, 
  },
  computed: {
  },
  methods: {
    fetchMovies() {
        const config = {
            headers: {
                Authorization: `Token ${this.$cookies.get('auth-token')}`
            },
        }
        axios.get(SERVER_URL + "movies/pick", config)
            .then(res => {
                this.movies = res.data
                console.log(res.data)
            })
            .catch(err => console.error(err))
    },
  },
  created() {
    this.fetchMovies()
    console.log(this)
  }
}

</script>

<style scoped>

</style>