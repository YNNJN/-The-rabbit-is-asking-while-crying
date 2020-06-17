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
          <button v-if="!isWatched(movie)" @click="watchedMovie(movie)" class="badge badge-light" data-toggle="modal" :data-target="'#scoremovie'+movie.DOCID">watched</button>
          <button v-if="isWatched(movie)" @click="watchedMovie(movie)" class="badge badge-light">watched</button>
          <img :src="movie.posters" class="card-img-top" :alt="movie.title">
        </div>
        <div class="modal fade" :id="'scoremovie'+movie.DOCID" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">{{ movie.title }}</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body">
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
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
              </div>
            </div>
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
      reviewData: {
        score: null,
        content: '',
      },
      user: Object,
    }
  },
  computed: {
    isWatched(movie) {
      return movie.watched.some(temp_watched => {
        temp_watched == this.user.id
      })    
    },
  },
  methods: {
    watchedMovie(movie) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        },
      }
      console.log(movie)
      axios.post(MOIVE_API_URL + `${movie.DOCID}/watched/`, movie, config)
      .then(res => console.log(res))
      .catch(err => console.error(err))
    },
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
        })
        .catch(err => console.log(err.response.data))
    },
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