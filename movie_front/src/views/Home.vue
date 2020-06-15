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
    <p class="lead text-center mt-5">가장 빠른 영화를 이곳에서 만나세요 !</p>
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

.thirty {
  height: 20rem;
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

</style>