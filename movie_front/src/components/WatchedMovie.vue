<template>
  <div class="watched_container">
    <div v-for="movie in movies" :key="movie.DOCID">
      <a class="watched_item text-decoration-none text-reset">{{ movie.title }}</a>
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
.watched_container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  width: 44rem;
  margin: auto;
}

.watched_item {
  background-color: paleturquoise;
  border-radius: 0.5rem;
  padding: 0.2rem;
  margin: 0.3rem;
  font-size: 0.9rem;
  font-family: 'NeoDunggeunmo';
  font-weight: normal;
  font-style: normal;
}

</style>