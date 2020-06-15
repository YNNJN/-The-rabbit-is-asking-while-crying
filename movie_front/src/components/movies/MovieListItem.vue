<template>
  <div class="movieListItem col-sm-12 col-md-4">
    <div class="card text-center p-2" width="100%">
      <p class="card-title text-secondary">- {{ movie.title }} -</p>
      <img :src="posterURL" class="card-img-top" :alt="movie.title">
      <div class="card-body">
        <button class="btn btn-info" data-toggle="modal" :data-target="'#movie'+movie.id">영화 상세보기</button>
      </div>
    </div>
    <MovieListItemModal :movie="movie"/>
  </div>
</template>

<script>
import MovieListItemModal from './MovieListItemModal.vue'
export default {
  name: 'MovieListItem',
  components: {
    MovieListItemModal
  },
  props: {
    movie: Object,
  },
  computed: {
    posterURL() {
      return this.movie.posters
    },
  }
}
</script>

<style>

</style>