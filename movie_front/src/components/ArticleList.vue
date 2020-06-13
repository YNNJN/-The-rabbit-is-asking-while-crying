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
          <tr v-for="(article, index) in reverse" :key="article.id">
            <th scope="row">{{ index+1 }}</th>
            <td>
              <button class="btn" data-toggle="modal" :data-target="articleModalId(article)" @click="addHits(article)">{{ article.title }}</button>
              <span v-if="index+1 == 1" class="badge badge-danger">New</span>
            </td>
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
                    <p v-for="comment in comments" :key="comment.id">{{ comment }}</p>
                    <hr>
                    <div class="input-group">
                      <input type="text" name="comment" class="form-control border-0 rounded-0 text-secondary" v-model="commentData.content" placeholder="댓글달기...">
                      <div class="input-group-append">
                        <button @click="createComment(article)" class="btn rounded-0 text-primary" type="submit">게시</button>
                      </div>
                    </div>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-warning" @click="onEdit(article)" data-dismiss="modal">Edit</button>
                    <button type="button" class="btn btn-danger" @click="ondelete(article)" data-dismiss="modal">Delete</button>
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
  name: 'ArticleList',
  data() {
    return {
      comments: [],
      commentData: {
        content: '',
      },
    }
  },
  props: {
    articles: {
      type: Array,
    },
    article: {
      type: Array,
    },
    isCreate: null,
  },
  computed: {
    reverse() {
      return this.articles.slice().reverse()
    },
  },
  methods: {
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
    },
    createComment(article) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(SERVER_URL + `articles/${article.id}/comment_create/`, this.commentData, config)
        .then(res => {
          console.log(res.data)
          this._data.comments.push(res.data.content)
          this._data.commentData.content = ''        
          // this.$router.push({ name: 'Detail', params: { article_pk: `article_${article.id}` }})
        })
        .catch(err => console.log(err))
    },
    onEdit(article) {
      this.article = article
      console.log(this)
      this.$emit('editData', this.article)
    },
    ondelete(article) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(SERVER_URL + `articles/${article.id}/delete/`, {}, config)
        .then(res => {
          console.log(res.data)
        })
        .catch(err => console.log(err))
    },
  },
}

</script>

<style>

</style>