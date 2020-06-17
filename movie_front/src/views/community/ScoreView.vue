<template>
    <div class="p-5">
        <p class="movie_title tag">{{ $route.query.movie.title }}</p>
        <div class="d-flex justify-content-center mb-5">
          <input type="checkbox" v-model="completed" class="mr-3" disabled><p class="watched_check">watched</p>
        </div>


        <v-card
          class="elevation-16 mx-auto"
          width="300"
        >
          <v-card-title
            class="headline"
            primary-title
          >
            <p class="rate_text"><strong>당신이 본 영화를 평가해주세요</strong></p>
          </v-card-title>
          <v-card-text>
            이곳에서 영화에 매긴 별점은 User Page의 My playlist에서 모두에게 보여질 수 있습니다
            <div class="text-center mt-12">
              <v-rating
                v-model="rating"
                color="yellow darken-3"
                background-color="grey darken-1"
                empty-icon="$ratingFull"
                half-increments
                hover
              ></v-rating>
            </div>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions class="justify-space-between">
            <v-btn text>No Thanks</v-btn>
            <v-btn
              color="primary"
              text
            >
              Rate Now
            </v-btn>
          </v-card-actions>
        </v-card>
        <div class="score_form">
          <div class="form-group">
              <label for="InputScore">Score</label>
              <input type="text" class="form-control" id="InputScore" v-model="reviewData.score">
          </div>
          <div class="form-group">
              <label for="InputContent">CONTENT</label>
              <input type="text" class="form-control" id="InputContent" v-model="reviewData.content" row="30">
          </div>
          <button type="submit" class="btn btn-success" @click="createReview($route.query.movie)">Create</button>
        </div>

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
        checked: true,
      },
      completed: true,
    }
  },
  computed: {},
  props: {
   
  },
  methods: {
    createReview(movie) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        },
      }
      console.log(movie)
      console.log(this)
      axios.post(MOIVE_API_URL + `movie/${movie.DOCID}/review_create/`, this.reviewData, config)
        .then(res => {
          console.log(res)
          this._data.reviewData.score=''
          this._data.reviewData.content=''
          console.log('yes')
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
      console.log(movie)
      axios.post(MOIVE_API_URL + `movie/${movie.DOCID}/watched/`, movie, config)
        .then(res => console.log(res))
        .catch(err => console.error(err))
    },
    deleteReview(movie) {
        const config = {
            headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
            },
        }
        axios.post(MOIVE_API_URL + `movie/${movie.DOCID}/watched/`, movie, config)
            .then(res => {
                console.log(res)
                this.$router.push('/community')
            })
            .catch(err => console.error(err))
    },
    onClick() {
      console.log(this)
    },
  },
  created() {
    console.log(this.$route.query.movie.watched)
    if (this.$route.query.movie.watched.some(temp_watched => {
        temp_watched == this.user})) {
        this.watchedMovie(this.$route.query.movie)
        this.deleteReview(this.$route.query.movie)
    } else {
        this.watchedMovie(this.$route.query.movie)
        console.log('no')
    }

    console.log(this.$route.query.movie.watched)
  },
}
</script>

<style>
.movie_title {
  color: seagreen;
  width: 20rem;
  border-radius: 0.8rem;
  font-size: 1.7rem;
  font-family: 'NeoDunggeunmo';
  font-weight: bold;
  font-style: normal;
  text-align: center;
  margin: auto;
}

.watched_check {
  color: slategray;
  text-align: center;
  font-family: 'NeoDunggeunmo';
  font-weight: bold;
  font-style: normal;
}

.rate_text {
  font-size: 1.1rem;
}

.score_form {
  padding-top: 3rem;
  width: 44rem;
  margin: auto;
}
</style>