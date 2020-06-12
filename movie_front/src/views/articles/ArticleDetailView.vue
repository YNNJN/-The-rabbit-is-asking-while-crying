<template>
  <div>
    <h1>Detail</h1>
    <div class="card mx-auto" style="width: 80%;">
        <div class="card-body">
            <h5 class="card-title">제목 : {{ $route.query.title }}</h5>
            <h5 class="cart-text">글쓴이 : {{ $route.query.user.username }}</h5>
            <p class="card-text">{{ $route.query.content }}</p>
        </div>
    </div>
    <div class="container text-left">
      <div class="form-group">
        <label for="InputTitle">Title</label>
        <input type="text" class="form-control" id="InputTitle" aria-describedby="titleHelp"  v-model="commentData.title">
        <small id="titleHelp" class="form-text text-muted">Please leave an opinion about the movie.</small>
      </div>
      <div class="form-group">
        <label for="InputContent">CONTENT</label>
        <input type="text" class="form-control" id="InputContent" v-model="commentData.content" row="30">
      </div>
      <button type="submit" class="btn btn-success" @click="createComment">Create</button>
    </div>
    <ArticleComment :comments="comments"/>
  </div>
</template>

<script>
import axios from 'axios'
import ArticleComment from '@/components/ArticleComment.vue'

const API_BASE_URL = "http://127.0.0.1:8000/"

export default {
    name: 'ArticleDetailView',
    components: {
        ArticleComment,
    },
    data() {
        return {
            comments: [],
            commentData: {
                title: '',
                content: '',
                created_at: Date.now(),
            },

        }    
    },    
    methods: {
        fetchArticleList() {
            const API_ARTICLE_LIST_URL = API_BASE_URL + "/articles/detail"
            axios.get(API_ARTICLE_LIST_URL)
                .then(res => {
                this.comments = res.data
                })
                .catch(err => {
                console.error(err)
                })
        },
        createComment() {
            const config = {
                headers: {
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
                }
            }
            axios.post(API_BASE_URL + `articles/${article.id}/create/`, this.commentData, config)
                .then(res => { 
                console.log(res.data)
                })
                .catch(err => console.log(err.response.data))
        },        
    },
    created() {
        this.fetchArticleList()
    },
}
</script>

<style>

</style>