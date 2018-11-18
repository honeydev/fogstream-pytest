<template>
    <div class="container">
        <div class="row">
            <div class="col-4 offset-4" style="margin-top: 10%">
            <form v-on:submit.prevent="sendForm()">
              <ul v-if="errors" class="error-messages list-unstyled">
                    <li v-for="error in errors" class="alert alert-danger" role="alert">{{ error }}</li>
              </ul>
              <div class="form-group">
                <label for="username">Username</label>
                <input v-model="username" type="text" class="form-control" id="username" aria-describedby="emailHelp" placeholder="Username">
              </div>
              <div class="form-group">
                <label for="password">Password</label>
                <input v-model="password" type="password" class="form-control" id="password" placeholder="Password">
              </div>
              <button class="btn btn-primary">Submit</button>
            </form>
                </div>
        </div>
    </div>
</template>


<script>

  import Axios from 'axios';
  import JWT from '../services/jwt';
  import ErrorsFormater from '../services/errorsFormater';

  const errorsFormater = new ErrorsFormater();

  export default {
      name: "login",
      data() {
        return {
            username: null,
            password: null,
            errors: []
        }
      },
      methods: {
          sendForm() {
              const username = this.username;
              const password = this.password;
              Axios.post('/api/login', {
                  username: username,
                  password: password
              }).then((response) => {
                  JWT.storeToken(response.data.token)
                  this.$router.push({ name: "contact-message" })
              }).catch((error) => {
                   if (error.response === undefined) {
                        return null
                   }
                   const formatedErrors = errorsFormater.format(error.response.data.errors);
                   this.setErrors(formatedErrors);
              });
          },
          setErrors(errors) {
              let newErrors = [];
              for (let errorsType in errors) {
                  newErrors = newErrors.concat(errors[errorsType])
              }
              this.errors = newErrors;
          }
      },
  }

</script>