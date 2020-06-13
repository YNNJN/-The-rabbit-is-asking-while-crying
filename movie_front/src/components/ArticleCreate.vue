<template>
  <div>
    <h1>Create</h1>
    <div class="container text-left">
      <div class="form-group">
        <label for="exampleInputTitle">Title</label>
        <input type="text" class="form-control" id="exampleInputTitle" aria-describedby="titleHelp" v-model="articleData.title">
        <small id="titleHelp" class="form-text text-muted">Please leave an opinion about the movie.</small>
      </div>
      <div class="form-group">
        <label for="exampleInputContent">CONTENT</label>
        <input type="text" class="form-control" id="exampleInputContent" v-model="articleData.content" row="30">
      </div>
      <button v-if="isCreate" type="submit" class="btn btn-success" @click="createArticle">Create</button>
      <button v-if="!isCreate" type="submit" class="btn btn-warning" @click="editArticle">Edit</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000/'

export default {
  name: "ArticleCreate",
  data() {
    return {
      articleData: {
        title: null,
        content: null,
        created_at: Date.now(),        
      },
    }
  },
  props: {
    article: {
      type: Array,
    },
    isCreate: null,
  },
  methods: {
    createArticle() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        },
      }
      axios.post(SERVER_URL + 'articles/create/', this.articleData, config)
        .then(res => { 
          console.log(res.data)
          console.log(this._data)
          this._data.articleData.title=''
          this._data.articleData.content=''
        })
        .catch(err => console.log(err.response.data))
    },
    editArticle() {
      console.log(this)
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        },
      }
      console.log(this.articleData)
      console.log(this.article)
      axios.post(SERVER_URL + `articles/${this.article.id}/update/`, this.articleData, config)
        .then(res => { 
          console.log(res.data)
          console.log(this._data)
          this._data.articleData.title=''
          this._data.articleData.content=''
          this.isCreate = true
          this.$emit('editCreate', this.isCreate)
        })
        .catch(err => console.log(err.response.data))
    },
  },
  created() {
    if (!this.$cookies.isKey('auth-token')) {
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<style>

</style>
