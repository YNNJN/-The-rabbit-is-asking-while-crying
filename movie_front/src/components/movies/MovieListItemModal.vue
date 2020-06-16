<template>
  <div class="movieListItemModal">    
    <div class="modal fade" :id="'movie'+movie.id" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">{{ movie.title }}</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <img :src="posterURL" class="img-fluid" alt='backdrop'>
            <hr>
            <p class="badge badge-light d-flex justify-content-center mb-3 p-2"> ⭐️</p>
            <p>{{ movie.plotText }}</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: "MovieListItemModal",
  props: {
    movie: Object
  },
  computed: {
    posterURL() {
      return this.movie.posters
    }
  },
}
</script>

<style>

</style>