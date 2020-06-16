<template>
  <div class="Community p-5">
    <div>
      <p class="lead">시간 떼우기 용도로 영화가 필요한 당신에게</p>
      <p class="lead">편향된 추천으로, 매번 비슷한 추천 목록에 지친 당신에게</p>
      <p class="lead">영화와 함께하는 짧은 휴식 후, 다음을 위한 활력을 얻고 싶은 당신에게</p>
    </div>
    <div class="p-3"></div>
    <div>
      <p class="lead">당신의 금쪽같은 시간을 지켜드려요</p>
      <p class="lead">기존의 자신이라면 선택하지 않았을지도 모르는 영화에서</p>
      <p class="lead">영감을 얻어요</p>
    </div>
    <p>임의의 영화리스트 제공</p>
    <div class="row p-3">
      <div v-for="movie in movies" :key="movie.DOCID" class="col-md-2">
        <div class="card_form card text-center p-2 border-0">
          <p class="card-title text-secondary"> {{ movie.title }}</p>
          <button @click="watchedMovie(movie.DOCID)" class="badge badge-light">watched</button>
          <img :src="movie.posters" class="card-img-top" :alt="movie.title">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const MOIVE_API_URL = 'http://127.0.0.1:8000/movies/'
export default {
  name: 'Community',
  data() {
    return {
      movies: [],
    }
  },
  methods: {
    watchedMovie(movie.DOCID) {
      console.log(movie.DOCID)
      axios.post(MOIVE_API_URL + movie.DOCID + '/watched/')
      .then(res => console.log(res))
      .catch(err => console.error(err))
    }
  },
  created() {
    const movie_list = []
    axios.get(MOIVE_API_URL)
    // 영화 리스트 랜덤 추출
    .then(res => {
      for (let i = 0; i < 12; i++) {
        movie_list[i] = res.data[Math.floor(Math.random() * 1622)]
      }
      // console.log(movie_list)
      this.movies = movie_list
      console.log(this.movies)
    })
    .catch(err => console.error(err))
  }
}
</script>

<style>

</style>