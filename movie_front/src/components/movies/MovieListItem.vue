<template>
  <div class="movieListItem col-sm-12 col-md-3">
    <div class="card text-center p-2 border-0">
      <p class="card-title text-secondary"> {{ movie.title }}</p>
      <img :src="posterURL" class="card-img-top" :alt="movie.title">
      <p class="badge badge-light">⏱{{ movie.runtime }}분</p>
      <div class="card-body">
        <button class="detail_button btn btn-secondary" data-toggle="modal" :data-target="'#movie'+movie.DOCID">자세히보기</button>
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
    MovieListItemModal,
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
.movieListItem {
  background-color: #1c1c38;
  border-radius: 0.5rem;
}

.card {
  background-color: #1c1c38;
}

.card-title {
  font-family: 'NeoDunggeunmo';
  font-weight: normal;
  font-style: normal;
}

.detail_button {
  font-size: 0.9rem;
  font-family: 'NeoDunggeunmo';
  font-weight: bold;
  font-style: normal;
}
</style>