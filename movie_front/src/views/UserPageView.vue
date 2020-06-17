<template>
  <div class="p-5">
    <div>
      <h1 class="page_title mb-5 text-center">User Page</h1>
      <p class="lead text-center">나의 플레이리스트를 설명해주세요</p>
    </div>
    <div class="jumbotron text-center p-3">
      <div class="d-inline">
        <img src="@/assets/anonymous.png" class="rounded-circle d-inine mr-5" widtn="90" height="90">
      </div>
      <div class="d-inline">
        <p class="lead d-inline mx-2" style="font-size: 1.8rem">{{ infos[1].username }}</p>
        <div class="d-inline btn btn-outline-dark btn-sm mx-2">Edit Profile</div>
        <i class="fas fa-cog mx-2"></i>
      </div>
      <!-- <div class="follow_text">
        <p class="d-inline mr-4">followers  |</p> 
        <p class="d-inline mr-4">following</p>
      </div> -->
    </div>
    <!-- 유저 목록, follow를 위해 버튼 클릭 -->
    <p class="text-center mt-5">다른 유저의 플레이리스트를 만나보세요 👉</p>
    <div class="d-flex justify-content-center">
      <span v-for="user in users" :key="user.username">
        <a @click="follow(user)" class="mx-3 text-decoration-none text-reset">{{ user.username }}</a>
      </span>
    </div>

    <ArticleCreate :article="article" :isCreate="isCreate" @editCreate="editCreate"/>
    <ArticleList :articles="articles" :isCreate="isCreate" @getArticle="getArticle()" @editData="onEdit"/>
    
    
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
      infos: [],
      users: [],
      username: [],
    }
  },
  props: {
    // follower: {
    //   type: Object,
    //   required: true,
    // },
    article: {
      type: Object,
    },
  },
  methods: {
    fetchArticles() {
      axios.get(SERVER_URL + "articles/")
        .then(res => this.articles = res.data)
        .catch(err => console.error(err))
    },
    getArticle() {
      this.fetchArticles()
    },
    onEdit(article) {
      this.article = article
      this.isCreate=false      
    },
    editCreate(isCreate) {
      this.isCreate = isCreate
    },
    getMyinfo() {
      axios.get(SERVER_URL + 'accounts/' + `${this.username}`)
      .then(res => {
        this.infos = res.data

      })
    },
    getUsers() {
      axios.get(SERVER_URL + 'accounts/')
      .then(res => {
        this.users = res.data
        for (let idx = 0; idx < this.users.length; idx ++) {
          this.username.push(this.users[idx].username)
        }
      })
    },
    follow(user) {
      axios.post(SERVER_URL + 'accounts/' + `${user.username}/` +'follow/')

      axios.get(SERVER_URL + 'accounts/' + `${user.username}/`) // back에서 문제가 있음, 해당 url에서 typeError
      .then(res => {
        console.log(res)
        console.log('test')
      })
    }
  },
  created() {
    this.fetchArticles()
  },
  mounted() {
    this.getMyinfo()
    this.getUsers()
  },
}
</script>

<style>
.page_title {
  color: #d8dcff;
  background-color: seagreen;
  border-radius: 0.5rem;
  width: 44rem;
  font-family: 'NeoDunggeunmo';
  font-weight: normal;
  font-style: normal;
  margin: auto;
}

.lead {
  color: #5d4c5f;
}

.jumbotron {
  margin: auto;
  width: 44rem;
}

.follow_text {
  margin-left: 6rem;
  margin-top: 0;
  color: #5d4c5f;
  font-family: 'NeoDunggeunmo';
  font-weight: normal;
  font-style: normal;
}

</style>