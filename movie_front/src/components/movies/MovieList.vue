<template>
  <div>
    <h1>MovieList</h1>
    <button @click="addmovie">영화 나와랏</button>
    <ul>
      <li v-for="movie in movies" :key="movie.id">
        <img :src="movie.posters" :alt="movie.title">
        <p>제목 : {{ movie.title }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MovieList',
  data() {
    return {
      movies: [],
    }
  },
  props: {
    Movies: Array,
  },
  methods: {
    addmovie() {
      axios.get('http://127.0.0.1:8000/movies/')
      .then(res=> {
        console.log(res.data[1].title) // 데이터가 100개 단위의 배열 형태로 저장되어있음
      })
    }
  },
  created () {
    axios.get('http://127.0.0.1:8000/movies/')
    .then(res => this.movies = res.data)
    .catch(err => console.error(err))
  }
}
</script>

<style>

</style>