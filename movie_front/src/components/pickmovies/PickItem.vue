<template>
  <div class="container">
    <div class="p-5">
      <v-card>
        <v-card-text>
          <v-slider @mousedown="onPoint(value)" v-model="value" label="How long?" :min="0" :max="140" append-icon="alarm" thumb-label ticks></v-slider>
        </v-card-text>
      </v-card>
      <div class="row p-3" v-if="show_on == true">
        <div v-for="ele in movie" :key="ele.DOCID" class="col-md-3">
          <div class="card_form card text-center p-2 border-0">
            <p class="card-title text-secondary"> {{ ele.title }}</p>
            <img :src="ele.posters" class="card-img-top" :alt="ele.title">
            <p class="badge badge-light">⏱{{ ele.runtime }}분</p>
            <div class="card-body">
              <button class="detail_button btn btn-secondary" data-toggle="modal" :data-target="'#movie'+ele.DOCID">자세히보기</button>
            </div>
          </div>
          <PickMovieDetail :ele="ele"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PickMovieDetail from './PickMovieDetail.vue'

export default {
  name: 'PickItem',
  components: {
    PickMovieDetail
  },
  props: {
    movies: {
      type: Array,
      required: true,
    },
  },
  data(){
    return {
      movie: [],
      show_on: false,
    }
  },
  methods: {
    onPoint(value) {
      console.log(value)
      this.movies.forEach(temp_movie => {
        if (temp_movie.runtime === value) {
          console.log(temp_movie)
          return this.movie.push(temp_movie)
        }
      })
      this.value = ''
      this.show_on = true
    },
  },
  computed: {

  }
}
</script>

<style scoped>
.card {
  background-color: #d8dcff;
}

.PickMovieDetail {
  background-color: #d8dcff;
  border-radius: 0.8rem;
}
</style>