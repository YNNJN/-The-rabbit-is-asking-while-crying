<template>
  <div class="container text-left">
    <h1>ee</h1>
    <div class="form-group">
      <label for="exampleInputTitle">Title</label>
      <input type="text" class="form-control" id="exampleInputTitle" aria-describedby="titleHelp" v-model="articleData.title">
      <small id="titleHelp" class="form-text text-muted">Please leave an opinion about the movie.</small>
    </div>
    <div class="form-group">
      <label for="exampleInputContent">CONTENT</label>
      <input type="text" class="form-control" id="exampleInputContent" v-model="articleData.content" row="30">
      </div>
    <button type="submit" class="btn btn-success" @click="createArticle">Create</button>
</div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000/'
export default {
  name: 'ReviewCreateView',
  data() {
    return {
      articleData: {
        title: null,
        content: null,
        created_at: Date.now(),
      }
    };
  },
  methods: {
    createArticle() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(SERVER_URL + 'articles/create/', this.articleData, config)
        .then(res => { 
          console.log(res.data) 
          this.$router.push({ name: 'List' })
        })
        .catch(err => console.log(err.response.data))
    },
  },
}
</script>

<style>

</style>