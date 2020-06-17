<template>
  <div class="Community p-5">
    <h1 class="page_title mb-5 text-center">watched</h1>
    <p class="lead text-center">랜덤으로 제공되는 영화 모음에 대해 '봤어요'를 표시하세요</p>
    <div class="p-4"></div>
    <div class="container p-0 pt-5 mt-5">
      <div class="row p-0 m-0">
        <div v-for="movie in movies" :key="movie.DOCID" class="col-md-2 p-0">
          <div class="card_box card text-center p-2 border-0">
            <p class="card_box_title"> {{ movie.title }}</p>
            <router-link :to="{ name: 'Score', query: { movie: movie } }"><button class="watched_button badge badge-success mb-2">watched</button></router-link>
            <img :src="movie.posters" class="card-img-top" :alt="movie.title">
          </div>
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
        if (this.user.age < 19) {
          if (movie_list[i].rating.slice(0,2) != 18 && movie_list[i].rating.slice(0,2) != "") {
            // console.log(movie_list[i].rating.slice(0,2))
            this.movies = movie_list
          }
        }
      }
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
    })
    .catch(err => console.log(err))
  }
}
</script>

<style scoped>
.card_box {
  background-color: #5d4c5f;
  border-radius: 0.8rem;
}

.card_box_title {
  color: #aeadf0;
  font-family: 'NeoDunggeunmo';
  font-weight: normal;
  font-style: normal;
}

</style>