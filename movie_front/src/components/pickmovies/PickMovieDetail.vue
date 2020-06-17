<template>
  <div class="PickMovieDetail">    
    <div class="modal fade bd-example-modal-lg" :id="'movie'+ele.DOCID" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg">
        <div class="modal-content container">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">{{ ele.title }} <p v-if="ele.titleEng.length" class="d-inline">({{ ele.titleEng }})</p></h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="row modal-body">
            <img :src="ele.posters" class="img-fluid" alt='ele.title' width="300">
            <div class="description col-sm-7 p-3 text-left">
              <p class="badge badge-light">{{ ele.genre }} {{ ele.rating }}</p>
              <p v-if="ele.directorNm.length"><strong class="tag">감독명:</strong> {{ ele.directorNm }}</p>
              <p v-if="ele.directorEnNm.length" class="mt-0">({{ ele.directorEnNm }})</p>
              <p v-if="ele.nation.length"><strong class="tag">제작국가:</strong> {{ ele.nation }}</p>
              <p v-if="ele.repRlsDate.length"><strong class="tag">개봉일자:</strong> {{ ele.repRlsDate }}</p>
              <p v-if="ele.keywords.length"><strong class="tag">키워드:</strong> {{ ele.keywords }}</p>
              <p v-if="ele.plotLang.length"><strong class="tag">줄거리 언어:</strong> {{ ele.plotLang }}</p>
              <p v-if="ele.plotText.length"><strong class="tag">줄거리:</strong> {{ ele.plotText }}</p>
            </div>
            <hr>
          </div>

          <div class="modal-footer">
            <button type="button" class="btn btn-secondary text-white" data-dismiss="modal">Close</button>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PickMovieDetail',
  props: {
    ele: Object
  }
}
</script>

<style>

</style>