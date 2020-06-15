<template>
  <div class="p-3">
    <h1 class="bold text-center">Movie List</h1>
    <ul>
      <!-- <li v-for="movie in movies" :key="movie.id">
        <img :src="movie.posters" :alt="movie.title">
        <p>제목 : {{ movie.title }}</p>
      </li> -->
    </ul>
    <div class="movieList row">
      <MovieListItem
        :movie="movie"
        v-for="movie in movies.slice(0,6)"
        :key="movie.id"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieListItem from './MovieListItem.vue'

export default {
  name: 'MovieList',
  components: {
    MovieListItem
  },
  props: {
    movies: Array,
  },
  methods: {

  },
  created () {
    axios.get('http://127.0.0.1:8000/movies/')
    .then(res => this.movies = res.data)
    .catch(err => console.error(err))
  }
}
</script>

<style>
.bold {
  color: #d8dcff;
  width: 100%;
  background-color: #1c1c38;
  font-family: 'NeoDunggeunmo';
  font-weight: bold;
  font-style: normal;

}
</style>