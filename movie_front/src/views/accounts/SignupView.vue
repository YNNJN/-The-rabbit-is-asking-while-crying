<template>
  <div class="p-5">
    <h1>SIGN UP</h1>
    <div class="container text-left">
      <div class="form-group">
        <label for="exampleInputID">ID</label>
        <input type="text" class="form-control" id="exampleInputID" v-model="signupInfo.username">
        <small id="idHelp" class="form-text text-muted">Please enter your ID</small>
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">PASSWORD</label>
        <input type="password" class="form-control" id="exampleInputPassword1" v-model="signupInfo.password">
        <small id="passwordHelp" class="form-text text-muted">The password must contain at least 8 characters and at least one special character. (e.g `, ~, !, @)</small>
      </div>
      <div class="form-group">
        <label for="exampleInputPassword2">PASSWORD CONFIRMATION</label>
        <input type="password" class="form-control" id="exampleInputPassword2" v-model="signupInfo.password2">
        <small id="passwordHelp" class="form-text text-muted">Please enter your password again.</small>
      </div>
      <div class="form-group">
        <label for="exampleInputAge">AGE</label>
        <input type="number" class="form-control" id="exampleInputAge" v-model="signupInfo.age">
        <small id="ageHelp" class="form-text text-muted">Please enter your age.</small>
      </div>
      <div class="form-group form-check">
        <input type="checkbox" class="form-check-input" id="exampleCheck1">
        <label class="form-check-label" for="exampleCheck1">Check me out</label>
      </div>
      <button type="submit" class="btn btn-success text-white mt-3" @click="emitSignupSubmit"><strong>Sign Up</strong></button>
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
        password: '',
        password2: '',
        age: null,
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