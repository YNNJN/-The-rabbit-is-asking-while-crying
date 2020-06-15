<template>
  <div class="p-5">
    <h1 class="mb-5 text-center">user page</h1>
    <ArticleList :articles="articles" :isCreate="isCreate" @editData="onEdit"/>
    <ArticleCreate :article="article" :isCreate="isCreate" @editCreate="editCreate"/>
  </div>
</template>

<script>
import axios from 'axios'
import ArticleCreate from '@/components/articles/ArticleCreate.vue'
import ArticleList from '@/components/articles/ArticleList.vue'

const SERVER_URL = 'http://127.0.0.1:8000/'

export default {
  name: 'UserPageView',
  components: {
    ArticleCreate,
    ArticleList,
  },
  data() {
    return {
      articles: [],
      isCreate: true,
    }
  },
  props: {
    follower: {
      type: Object,
      required: true,
    },
    article: {
      type: Array,
    },
  },
  methods: {
    fetchArticles() {
      axios.get(SERVER_URL + "articles/")
        .then(res => this.articles = res.data)
        .catch(err => console.error(err))
    },
    onEdit(article) {
      this.article = article
      this.isCreate=false      
    },
    editCreate(isCreate) {
      this.isCreate = isCreate
    },
  },
  created() {
    this.fetchArticles()
  },
}
</script>

<style>

</style>