<template>
  <div id="app" class="back">
    <nav class="navbar navbar-expand-lg sticky-top p-5">
      <div class="navbar" style="position: absolute; left: 50%; transform: translateX(-50%);">
        <router-link to="/" class="text-dark text-decoration-none pt-5"><strong>토끼가 울며 여짜오되</strong></router-link>
      </div>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse d-flex justify-content-between" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link class='nav-link pt-5' to="/articles">Community</router-link>
          </li>
          <li class="nav-item">
            <router-link v-if="isLoggedIn" class='nav-link pt-5' to="/articles/create">New</router-link>
          </li>
        </ul>
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link v-if="!isLoggedIn" class='nav-link pt-5' to="/accounts/signup">Signup</router-link>
          </li>
          <li class="nav-item">
            <router-link v-if="!isLoggedIn" class='nav-link pt-5' to="/accounts/login">Login</router-link>
          </li>
          <li class="nav-item">
            <router-link v-if="isLoggedIn" class='nav-link pt-5' to="/accounts/userpage">Userpage</router-link>
          </li>
          <li class="nav-item">
            <router-link v-if="isLoggedIn" @click.native="logout" class='nav-link pt-5' to="/accounts/logout">Logout</router-link>
          </li>
        </ul>
      </div>
    </nav>

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
  font-size: 1.3rem;
}

.back {
  min-height: 100vh;
  background: #020815;
}

.navbar {
  background: #020815;
}

.nav-item {
  font-size: 0.9rem;
}

.nav-link {
  color: #c5fb20;
  font-family: 'NeoDunggeunmo';
  font-weight: normal;
  font-style: normal;
}

strong {
  color: #c5fb20;
  font-size: 1.5rem;
  font-family: 'NeoDunggeunmo';
  font-weight: normal;
  font-style: normal;
}
</style>

