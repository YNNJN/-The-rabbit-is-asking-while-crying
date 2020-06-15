<template>
  <div class="container">
    <div class="p-5">
      <v-card>
        <v-card-text>
          <v-slider @mousedown="onPoint(value)" v-model="value" label="How long?" :min="3" :max="140" thumb-label step="10" ticks></v-slider>
        </v-card-text>
      </v-card>
    </div>
    <div class="row">
      <div class="thirty col-6 text-center">
        <button type="button" class="btn text-dark" data-toggle="modal" data-target="#minuteModal">
          <p>30 min</p>
        </button>
      </div>
      <div class="sixty col-6 text-center">
        <button type="button" class="btn text-dark" data-toggle="modal" data-target="#hourModal">
          <p>60 min</p>
        </button>
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
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
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
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
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