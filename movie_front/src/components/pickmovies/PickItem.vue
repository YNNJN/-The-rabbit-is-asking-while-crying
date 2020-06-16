<template>
  <div class="container">
    <div class="p-5">
      <v-card>
        <v-card-text>
          <v-slider @mousedown="onPoint(value)" v-model="value" label="How long?" :min="3" :max="140" thumb-label step="10" ticks></v-slider>
        </v-card-text>
      </v-card>
    </div>
    <PickMovieDetail/>
  </div>
</template>

<script>
import PickMovieDetail from '@/components/pickmovies/PickMovieDetail.vue'

export default {
  name: 'PickItem',
  components: {
      PickMovieDetail,
  },
  methods: {
    onPoint(value) {
      console.log(value)
    }
  },
}
</script>

<style>
.thirty {
  height: 20rem;
  background-color: slategrey;
  padding: 5rem;
  font-size: 1.5rem;
  font-family: 'NeoDunggeunmo';
  font-weight: normal;
  font-style: normal;
}
.sixty {
  height: 20rem;
  background-color: seagreen;
  padding: 5rem;
  font-size: 1.5rem;
  font-family: 'NeoDunggeunmo';
  font-weight: normal;
  font-style: normal;
}
</style>