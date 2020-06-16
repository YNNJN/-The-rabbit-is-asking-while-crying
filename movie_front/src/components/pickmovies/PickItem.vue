<template>
  <div class="container">
    <div class="p-5">
      <v-card>
        <v-card-text>
          <v-slider @mousedown="onPoint(value)" v-model="value" label="How long?" :min="3" :max="140" thumb-label step="10" ticks></v-slider>
        </v-card-text>
      </v-card>
      <div class="search_result p-3" v-if="show_on == true">
        <p>찾았다 영화</p>
        <p>{{ movie.title }}</p>
        <p>{{ movie.runtime }}</p>
        <img :src="movie.posters" width="200px" alt="movie.title">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PickItem',
  props: {
    movies: {
      type: Array,
      required: true,
    },
  },
  data(){
    return {
      movie: '',
      show_on: false,
    }
  },
  methods: {
    onPoint(value) {
      console.log(value)
      this.movies.forEach(temp_movie => {
        if (temp_movie.runtime === value) {
          console.log(temp_movie)
          return this.movie = temp_movie
        }
      })
      this.show_on = true
      // this.movies.forEach(temp_movie => {
      //   if (temp_movie.runtime.includes(value) === true)
      //     return this.movie = temp_movie
      // })
      // this.show_on = true
    },
  },
  computed: {
    // 범위 +- 5min
  }
}
</script>

<style>

</style>