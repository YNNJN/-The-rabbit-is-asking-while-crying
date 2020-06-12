<template>
  <div>
    <h1>Detail</h1>
    <div class="card mx-auto" style="width: 80%;">
        <div class="card-body">
            <h5 class="card-title">제목 : {{ $route.query.title }}</h5>
            <h5 class="cart-text">글쓴이 : {{ $route.query.user.username }}</h5>
            <p class="card-text">{{ $route.query.content }}</p>
        </div>
        <button @click="onData">check</button>
    </div>
    <ArticleCommentView :comments="comments"/> // 이안에 이것으로 받아오는게 있었습니다. @comment_data="createComment"
  </div>
</template>

<script>
import axios from 'axios'
import ArticleCommentView from '@/components/ArticleCommentView.vue'

const API_BASE_URL = "http://localhost:8000"

export default {
    name: 'ArticleDetailView',
    components: {
        ArticleCommentView,
    },
    data() {
        return {
            comments: [],
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
    //     createComment() {
    //         const config = {
    //             headers: {
    //                 Authorization: `Token ${this.$cookies.get('auth-token')}`
    //             }
    //         }
    //         axios.post(API_BASE_URL + `articles/${this.$route.query.id}/create/`, this.articleData, config)
    //             .then(res => { 
    //             console.log(res.data)
    //             this.$router.push({ name: 'detail', params: { articleId: ''} })
    //             })
    //             .catch(err => console.log(err.response.data))
    //     },
    },
    created() {
        this.fetchArticleList()
    },
}
</script>

<style>

</style>