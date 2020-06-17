<template>
  <div class="Community p-5">
    <div class="ad_1 float-right">
      <p class="lead">당신의 금쪽같은 시간을 지켜드려요</p>
      <p class="lead">기존의 자신이라면 선택하지 않았을지도 모르는 영화에서</p>
      <p class="lead">영감을 얻어요</p>
    </div>
    <div class="ad_2">
      <p class="lead">시간 떼우기 용도로 영화가 필요한 당신에게</p>
      <p class="lead">편향된 추천으로, 매번 비슷한 추천 목록에 지친 당신에게</p>
      <p class="lead">영화와 함께하는 짧은 휴식 후, 다음을 위한 활력을 얻고 싶은 당신에게</p>
    </div>
    <p>임의의 영화리스트 제공</p>
    <div class="row p-3">
      <div v-for="movie in movies" :key="movie.DOCID" class="col-md-2">
        <div class="card_form card text-center p-2 border-0">
          <p class="card-title text-secondary"> {{ movie.title }}</p>
          <router-link :to="{ name: 'Score', query: { movie: movie } }"><button class="badge badge-light">watched</button></router-link>
          <img :src="movie.posters" class="card-img-top" :alt="movie.title">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const MOIVE_API_URL = 'http://127.0.0.1:8000/movies/'
const USER_API_URL = 'http://127.0.0.1:8000/accounts/user_info/'

export default {
  name: 'Community',
  data() {
    return {
      movies: [],
      user: Object,
    }
  },
  methods: {
    
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
      console.log(res)
      console.log(this.movies)
    })
    .catch(err => console.error(err))
    const config = {
      headers: {
        Authorization: `Token ${this.$cookies.get('auth-token')}`
      },
    }
    axios.get(USER_API_URL, config)
    .then(res => {
      this.user = res.data
      console.log(this.user)
    })
    .catch(err => console.log(err))
    console.log(this)
  }
}
</script>

<style>
.ad_1 {
  border-radius: 0.5rem;
  border-left: thick solid #d8dcff;
  padding: 2rem;
}

.ad_2 {
  border-radius: 0.5rem;
  border-left: thick solid palegreen;
  padding: 2rem;
}

</style>