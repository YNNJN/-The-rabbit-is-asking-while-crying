<template>
  <div>
    <h1>SIGN UP</h1>
    <div class="container text-left">
      <div class="form-group">
        <label for="exampleInputID">ID</label>
        <input type="text" class="form-control" id="exampleInputID" v-model="signupInfo.username">
        <small id="idHelp" class="form-text text-muted">Please enter your ID</small>
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">PASSWORD</label>
        <input type="password" class="form-control" id="exampleInputPassword1" v-model="signupInfo.password1">
        <small id="passwordHelp" class="form-text text-muted">The password must contain at least 8 characters and at least one special character. (e.g `, ~, !, @)</small>
      </div>
      <div class="form-group">
        <label for="exampleInputPassword2">PASSWORD CONFIRMATION</label>
        <input type="password" class="form-control" id="exampleInputPassword2" v-model="signupInfo.password2">
        <small id="passwordHelp" class="form-text text-muted">Please enter your password again.</small>
      </div>
      <div class="form-group form-check">
        <input type="checkbox" class="form-check-input" id="exampleCheck1">
        <label class="form-check-label" for="exampleCheck1">Check me out</label>
      </div>
      <button type="submit" class="btn btn-info" @click="emitSignupSubmit">Sign Up</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignupView',
  data() {
    return {
      signupInfo: {
        username: '',
        password1: '',
        password2: '',
      },
    }
  },
  methods: {
    emitSignupSubmit() {
      this.$emit('signup-submit', this.signupInfo)
    }
  }
}
</script>

<style>

</style>