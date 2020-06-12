<template>
  <div>
    <h1>Comment</h1>
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
  props: {
    comments: {
      type: Array,
    },
    commentData: {
        title: '',
        content: '',
        created_at: Date.now(),
    },
  },
  methods: {
    onComment() {
      this.$emit('comment_data', this.commentData)
      this.commentData.title = ''
      this.commentData.content = ''
    },
  },
}
</script>

<style>

</style>
