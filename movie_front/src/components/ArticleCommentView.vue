<template>
  <div>
    <h1>Comment</h1>
    <div class="container text-left">
      <div class="form-group">
        <label for="exampleInputTitle">Title</label>
        <input type="text" class="form-control" id="exampleInputTitle" aria-describedby="titleHelp" v-model="commentData.title">
        <small id="titleHelp" class="form-text text-muted">Please leave an opinion about the movie.</small>
      </div>
      <div class="form-group">
        <label for="exampleInputContent">CONTENT</label>
        <input type="text" class="form-control" id="exampleInputContent" v-model="commentData.content" row="30">
      </div>
      <button type="submit" class="btn btn-success" @click="onComment">Comment Create</button>
    </div>
    <div class="card mx-auto" style="width: 80%;">
        <div class="card-body">
          <div v-for="comment in comments" :key="comment.id">
            <h5 class="cart-text">글쓴이 : {{ comment.user.username }}</h5>
            <p class="card-text">{{ comment.content }}</p>
          </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ArticleCommentView',
  peops: {
    comments: {
      type: Array,
    },
    commentData: {
        title: null,
        content: null,
        created_at: Date.now(),
    },
  },
  methods: {
    onComment() {
      this.$emit('comment_data', this.commentData)
      this.commentData.title = null
      this.commentData.content = null
    },
  },
}
</script>

<style>

</style>