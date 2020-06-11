<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link v-if="!isLoggedIn" to="/accounts/signup">Signup</router-link> | 
      <router-link v-if="!isLoggedIn" to="/accounts/login">Login</router-link>
      <router-link @click.native="logout" v-if="isLoggedIn" to="/accounts/logout">Logout</router-link> 
    </div>
    <router-view
      @login-submit="login"
      @signup-submit="signup"
    />
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000/'

export default {
  name: 'App',
  data() {
    return {
      isLoggedIn : false,
    }
  },
  methods: {
    setCookie(key) {
      this.$cookies.set('auth-token', key)
    },
    login(userInfo) {
      axios.post(SERVER_URL + 'rest-auth/login/', userInfo)
        .then(res => {
          const Key = res.data.key
          this.setCookie(Key)
          this.isLoggedIn = true
          this.$router.push({ name: 'Home' })
        })
        .catch(err => {
          console.log(err.response.data)
        })
    },
    logout() {
      const requestHeaders = {
        headers : {
          'Authorization' : `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(SERVER_URL + 'rest-auth/logout/', null, requestHeaders)
        .then(() => {
          this.$cookies.remove('auth-token')
          this.isLoggedIn = false
          this.$router.push({ name: 'Home'})
        })
    },
    signup(signupInfo) {
      axios.post(SERVER_URL + 'rest-auth/signup/', signupInfo)
        .then(() => {
          this.$router.push({ name: 'Home'})
        })
        .catch(err => [
          console.log(err.response.data)
        ])
    },
    created() {
      if (this.$cookies.isKey('auth-token')) {
        this.isLoggedIn = true
      }
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #1F45FC;
}
</style>
