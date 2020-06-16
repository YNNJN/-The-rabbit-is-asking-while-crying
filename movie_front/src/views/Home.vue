<template>
  <div class="home">
    <div class="p-5">
      <div class="d-flex justify-content-center">
        <div class="thirty text-center m-2">
          <button type="button" class="btn text-dark" data-toggle="modal" data-target="#minuteModal">
            <p style="font-size:2.5rem">30 min</p>
            <img class="rabbit_icon" src="@/assets/rabbit_sleeping.png">
          </button>
        </div>
        <div class="sixty text-center m-2">
          <button type="button" class="btn text-dark" data-toggle="modal" data-target="#hourModal">
            <p style="font-size:2.5rem">60 min</p>
            <img class="turtle_icon" src="@/assets/turtle.png">
          </button>
        </div>
      </div>
    </div>
    <div class="modal fade" id="minuteModal" tabindex="-1" role="dialog" aria-labelledby="minuteModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="minuteModalLabel">Modal title</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <PickMovieDetail/>
          </div>
        </div>
      </div>
    </div>
    <div class="modal fade" id="hourModal" tabindex="-1" role="dialog" aria-labelledby="hourModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="hourModalLabel">Am Modal title</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <PickMovieDetail/>
          </div>
        </div>
      </div>
    </div>


    <div class="p-3">
      <p class="lead text-center mt-5">가장 빠른 영화를 이곳에서 만나세요 !</p>
      <button v-if="showButton" @click="getMovieData" class="start_button btn"><strong>start</strong></button>
    </div>
    <div class="list_up container mt-5 p-0">
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
      showButton: true,
    }
  },
  methods: {
    getMovieData() {
      this.showButton = false
      axios.get(MOIVE_API_URL)
      .then(res => {
        this.movies = res.data
        console.log(this.movies)
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  // created () {
  //   axios.get(MOIVE_API_URL)
  //   .then(res => this.movies = res.data)
  //   .catch(err => console.error(err))
  // }
}
</script>
<style>
.lead {
  font-family: 'NeoDunggeunmo';
  font-weight: normal;
  font-style: normal;
}

.thirty {
  height: 20rem;
  width: 20rem;
  background-color: slategrey;
  border-radius: 0.5rem;
  font-size: 1.5rem;
  font-family: 'NeoDunggeunmo';
  font-weight: normal;
  font-style: normal;
  transition: 0.5s;
}

.thirty:hover {
  transform: scale(1.2) rotate(-10deg);
  opacity: 0.9;
}

.sixty {
  height: 20rem;
  width: 20rem;
  background-color: seagreen;
  border-radius: 0.5rem;
  font-size: 1.5rem;
  font-family: 'NeoDunggeunmo';
  font-weight: normal;
  font-style: normal;
  transition: 0.5s;
}

.sixty:hover {
  transform: scale(1.2) rotate(10deg);
  opacity: 0.9;
}

.rabbit_icon {
  margin-top: 1.5rem;
  width: 150px;
  height: 225px;
}

.turtle_icon {
  width: 160px;
  height: 240px;
}

.start_button {
  display: block;
  background-color: #d8dcff;
  font-size: 1.2rem;
  font-family: 'NeoDunggeunmo';
  font-weight: bold;
  font-style: normal;
  margin: auto;
}
</style>