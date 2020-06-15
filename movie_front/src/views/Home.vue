<template>
  <div class="home">
    <div class="p-5">
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
    </div>
    <div class="MovieView container">
      <MovieList :movies="movies"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieList from '@/components/movies/MovieList.vue'

const MOIVE_API_URL = 'http://127.0.0.1:8000/movies/'
export default {
  name: 'Home',
  components: {
    MovieList,
  },
  data() {
    return {
      movies: [],
    }
  },
  props: {
    Movies: Array,
  },
  methods: {
    getMovieData() {
      axios.get(MOIVE_API_URL)
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  created () {
    axios.get(MOIVE_API_URL)
    .then(res => this.movies = res.data)
    .catch(err => console.error(err))
  }
}
</script>
<style>
.lead {
  font-family: 'NeoDunggeunmo';
  font-weight: normal;
  font-style: normal;
}

</style>