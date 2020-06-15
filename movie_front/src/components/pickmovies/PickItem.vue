<template>
    <div class="container">
        <div class="row">
            <div class="border border-white col-5 text-center">
                <button type="button" class="btn text-white" data-toggle="modal" data-target="#minuteModal">
                    30 Minute
                </button>
            </div>
            <div class="col-2"></div>
            <div class="border border-white col-5 text-center">
                <button type="button" class="btn text-white" data-toggle="modal" data-target="#hourModal">
                    An hour
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
}
</script>

<style>

</style>