<template>
  <div class="MovieScoreModal">
    <div class="modal fade" :id="'scoremovie'+movie.DOCID" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">{{ movie.title }}</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <p>하...</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            <button type="button" class="btn btn-secondary" @click="onClick">Check</button>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: "MovieScoreModal",
  props: {
    movie: Object
  },
  computed: {
  },
  methods: {
    onClick() {
      console.log(this)
    },
  },
}
</script>

<style>

</style>