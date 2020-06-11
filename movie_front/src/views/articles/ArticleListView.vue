<template>
  <div>
    <h1>BOARDS</h1>
    <div class="container mt-3">
      <table class="table table-hover ">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">TITLE</th>
            <th scope="col">USER</th>
            <th scope="col">HITS</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="( article, index ) in reverse" :key="article.id">
            <th scope="row">{{ index+1 }}</th>
            <td><button class="btn" data-toggle="modal" :data-target="articleModalId(article)" @click="addHits(article)">{{ article.title }}</button> <span v-if="index+1 == 1" class="badge badge-danger">New</span></td>
            <div class="modal fade" :id="modalId(article)" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog" role="document">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">{{ article.title }}</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                      <span aria-hidden="true">&times;</span>
                    </button>
                  </div>
                  <div class="modal-body">
                    <p>{{ article.content }}</p>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                  </div>
                </div>
              </div>
            </div>
            <td>{{ article.user.username }}</td>
            <td>{{ article.hits }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000/'

export default {
  name: 'ArticleListView',
  data() {
    return {
      articles: [],
    }
  },
  computed: {
    reverse() {
      return this.articles.slice().reverse()
    },
  },
  methods: {
    fetchArticles() {
      axios.get(SERVER_URL + "articles/")
        .then(res => this.articles = res.data)
        .catch(err => console.error(err))
    },
    articleModalId(article) {
      return `#article_${article.id}`
    },
    modalId(article) {
      return `article_${article.id}`
    },
    addHits(article) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      article.hits++
      axios.put(SERVER_URL + `articles/hits/${article.id}/`, article, config)
        .catch(err => console.log(err))
    }
  },
  created() {
    this.fetchArticles()
  },
}

</script>

<style>

</style>