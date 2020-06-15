<template>
  <div>
    <h1 class="bold mb-4 text-center">Movie List</h1>
    <div class="movieList row">
      <MovieListItem
        :movie="movie"
        v-for="movie in movies.slice(0,8)"
        :key="movie.id"
      />
    </div>
  </div>
</template>

<script>
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
}
</script>

<style>
.bold {
  color: #d8dcff;
  background-color: #1c1c38;
  width: 44rem;
  margin: auto;
  font-family: 'NeoDunggeunmo';
  font-weight: bold;
  font-style: normal;
}
</style>