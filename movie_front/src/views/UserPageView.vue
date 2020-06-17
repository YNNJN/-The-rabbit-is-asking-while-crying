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
        <p class="lead d-inline mx-2" style="font-size: 1.8rem">{{ user_info.username }}</p>
        <div class="d-inline btn btn-outline-dark btn-sm mx-2">Edit Profile</div>
        <i class="fas fa-cog mx-2"></i>
      </div>
    </div>
    <!-- 유저 목록, follow를 위해 버튼 클릭 -->
    <p class="playlist_text text-center mt-5">다른 유저의 플레이리스트를 만나보세요 👉</p>
    <div class="d-flex justify-content-center">
      <span v-for="user in users" :key="user.username">
        <a @click="follow(user)" class="badge badge-pill badge-light mx-3 text-decoration-none text-reset">{{ user.username }}</a>
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
const USER_API_URL = 'http://127.0.0.1:8000/accounts/user_info/'

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
      users: [],
      username: [],
      user_info: Object,
      following_users: [],
      followed: false,
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
    // all users list
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
      axios.post(SERVER_URL + 'accounts/profile/' + `${user.username}/` +'follow/') // follow
      .then(res => {
        this.followed = true
        console.log(res)
        console.log('sss')
      })

      axios.get(SERVER_URL + 'accounts/profile/' + `${user.username}/`) // profile
      .then(res => {
        const name_list = res.data.followers
        const temp = []
        for (let idx = 0; idx < name_list.length; idx++) {
          const user_name = name_list[idx]
          axios.get(SERVER_URL + 'accounts/profile/' + `${user_name}/`)
          .then(res => {
            temp.push(res.data)
          })
        }
        this.following_users = temp
      })
      .catch(err => console.log(err))
    }
  },
  created() {
    this.fetchArticles()

    // get my information
    const config = {
      headers: {
        Authorization: `Token ${this.$cookies.get('auth-token')}`
      },
    }
    axios.get(USER_API_URL, config)
    .then(res => {
      this.user_info = res.data
      // console.log(this.user_info)
    })
    .catch(err => console.log(err))
  },

  mounted() {
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

.playlist_text {
  color: #5d4c5f;
  padding-top: 4rem;
  font-size: 1.1rem;
  font-family: 'NeoDunggeunmo';
  font-weight: normal;
  font-style: normal;
}
</style>