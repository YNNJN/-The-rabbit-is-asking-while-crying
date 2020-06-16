<template>
  <div>
    <div class="container text-left">
      <div class="p-5 mx-5">
        <div class="form-group">
          <label for="exampleInputTitle">Title</label>
          <input type="text" class="form-control" id="exampleInputTitle" aria-describedby="titleHelp" v-model="articleData.title">
          <small id="titleHelp" class="form-text text-muted">Please leave an opinion about the movie.</small>
        </div>
        <div class="form-group">
          <label for="exampleInputContent">CONTENT</label>
          <textarea class="form-control" id="exampleInputContent" v-model="articleData.content" row="10"></textarea>
        </div>
        <div class="button_group">
          <button v-if="isCreate" type="submit" class="btn btn-success text-white" @click="createArticle"><strong>Create</strong></button>
          <button v-if="!isCreate" type="submit" class="btn btn-warning" @click="editArticle"><strong>Edit</strong></button>
        </div>
      </div>
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
    getArticle() {
      this.$emit('getArticle', this.isCreate)
    },
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
          this.getArticle()
        })
        .catch(err => console.log(err.response.data))
        // .then(() =>{
        //   this.$router.go()
        // })
    },
    editArticle(article) {
      console.log(article)
      console.log(this)
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        },
      }
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

<style scoped>
.form-group {
  width: 44rem;
  margin: auto;
}

.button_group {
  margin-left: 10rem;
  margin-top: 1rem;
}

</style>
