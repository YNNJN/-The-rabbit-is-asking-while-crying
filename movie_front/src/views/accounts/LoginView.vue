<template>
  <div>
    <h1 class="p-5">LOG IN</h1>
    <div class="container text-left">
      <div class="form-group">
        <label for="exampleInputID">ID</label>
        <input type="text" class="form-control" id="exampleInputID" aria-describedby="idHelp" v-model="loginInfo.username">
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">PASSWORD</label>
        <input type="password" class="form-control" id="exampleInputPassword1" v-model="loginInfo.password">
      </div>
      <button type="submit" class="btn btn-warning" @click="emitLoginSubmit">Log In</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'loginView',
  data() {
    return {
      loginInfo : {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    emitLoginSubmit() {
      this.$emit('login-submit', this.loginInfo)
    },
    created() {
      if (this.$cookies.isKey('auth-token')) {
        this.$router.push({ name: 'Home'})
      }
    },
  }
}
</script>
