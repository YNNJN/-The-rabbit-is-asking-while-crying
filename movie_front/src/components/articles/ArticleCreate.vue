<template>
  <div>
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
     <button type="submit" class="btn btn-white" @click="check">check</button>
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
        title: '',
        content: '',
        created_at: Date.now(),        
      },
    }
  },
  props: {
    article: {
      type: Object,
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
          console.log(event.target.value)
        })
        .catch(err => console.log(err.response.data))
        .then(() =>{
          this.$router.go()
        })
    },
    editArticle(article) {
      console.log(article)
      console.log(this)
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        },
      }
      console.log(this.articleData)
      console.log(this.article)
      axios.post(SERVER_URL + `articles/${article.id}/update/`, this.articleData, config)
        .then(res => { 
          console.log(res.data)
          console.log(this._data)
          this._data.articleData.title=''
          this._data.articleData.content=''
          this.isCreate = true
          this.$emit('editCreate', this.isCreate)
        })
        .catch(err => console.log(err.response.data))
        .then(() =>{
          this.$router.go()
        })
    },
    check() {
      console.log(this)
    },
  },
  created() {
    if (!this.$cookies.isKey('auth-token')) {
      this.$router.push({ name: 'Login' })
    }
    if (!this.isCreate) {
      console.log(this.articleData)
      console.log(this.article)
      this.articleData.title = this.article.title
      this.articleData.content = this.article.content
      console.log(this.articleData)
    } else {
      console.log(this.articleData)
    }
  }
}
</script>

<style>

</style>
