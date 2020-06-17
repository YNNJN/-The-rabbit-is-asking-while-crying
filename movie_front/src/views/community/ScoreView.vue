<template>
    <div class="p-5">
        <p>{{ $route.query.movie.title }}</p>
        <div class="form-group">
            <label for="InputScore">Score</label>
            <input type="text" class="form-control" id="InputScore" v-model="reviewData.score">
        </div>
        <div class="form-group">
            <label for="InputContent">CONTENT</label>
            <input type="text" class="form-control" id="InputContent" v-model="reviewData.content" row="30">
        </div>
        <button type="submit" class="btn btn-success" @click="createReview(movie)">Create</button>
    </div>
</template>

<script>
import axios from 'axios'

const MOIVE_API_URL = 'http://127.0.0.1:8000/movies/'

export default {
  name: 'ScoreView',
  data() {
    return {
      reviewData: {
        score: null,
        content: '',
      },
    }
  },
  props: {
   
  },
  methods: {
    createReview(movie) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        },
      }
      axios.post(MOIVE_API_URL + `${movie.DOCID}/review_create/`, this.reviewData, config)
        .then(res => {
          console.log(res) 
          this._data.reviewData.score=''
          this._data.reviewData.content=''
          this.$router.push('/community')
        })
        .catch(err => console.log(err.response.data))
    },
    watchedMovie(movie) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        },
      }
      axios.post(MOIVE_API_URL + `${movie.DOCID}/watched/`, movie, config)
        .then(res => console.log(res))
        .catch(err => console.error(err))
    },
  },
  created() {
    console.log(this.$route.query.movie.watched)
    if (this.$route.query.movie.watched.some(temp_watched => {
        temp_watched == this.user})) {
        this.watchedMovie(this.$route.query.movie)
        this.$router.go(-1)
    } else {
        this.watchedMovie(this.$route.query.movie)
        console.log('no')
    }

    console.log(this.$route.query.movie.watched)
  },
}
</script>

<style>


</style>