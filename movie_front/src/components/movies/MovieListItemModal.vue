<template>
  <div class="movieListItemModal">    
    <div class="modal fade bd-example-modal-lg" :id="'movie'+movie.DOCID" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg">
        <div class="modal-content container">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">{{ movie.title }} <p v-if="movie.titleEng.length" class="d-inline">({{ movie.titleEng }})</p></h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="row modal-body">
            <img :src="posterURL" class="img-fluid" alt='movie.title' width="300">
            <div class="description col-sm-7 p-3 text-left">
              <p class="badge badge-light">{{ movie.genre }} {{ movie.rating }}</p>
              <p v-if="movie.directorNm.length"><strong class="tag">감독명:</strong> {{ movie.directorNm }}</p>
              <p v-if="movie.directorEnNm.length" class="mt-0">({{ movie.directorEnNm }})</p>
              <p v-if="movie.nation.length"><strong class="tag">제작국가:</strong> {{ movie.nation }}</p>
              <p v-if="movie.repRlsDate.length"><strong class="tag">개봉일자:</strong> {{ movie.repRlsDate }}</p>
              <p v-if="movie.keywords.length"><strong class="tag">키워드:</strong> {{ movie.keywords }}</p>
              <p v-if="movie.plotLang.length"><strong class="tag">줄거리 언어:</strong> {{ movie.plotLang }}</p>
              <p v-if="movie.plotText.length"><strong class="tag">줄거리:</strong> {{ movie.plotText }}</p>
            </div>

            <hr>
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
  methods: {

  },
}
</script>

<style>
.description {
  font-size: 1rem;
}

.tag {
  background-color: paleturquoise;
  padding: 0.2rem;
}
</style>