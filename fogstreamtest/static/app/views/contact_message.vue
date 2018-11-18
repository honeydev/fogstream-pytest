<template>
    <div class="container">
        <div class="row">
            <div class="col-8 offset-2" style="margin-top: 10%">
            <p v-if="sended">The message is successfully sent to the administrator</p>
            <form v-else v-on:submit.prevent="sendForm()">
                <ul v-if="errors" class="error-messages list-unstyled">
                    <li v-for="error in errors" class="alert alert-danger" role="alert">{{ error }}</li>
                 </ul>
                <div class="form-group">
                   <label for="title">Title</label>
                   <input v-model="title" type="text" class="form-control" id="title" placeholder="Enter title">
                </div>
                <div class="form-group">
                    <label for="body">Message text</label>
                   <textarea v-model="body" id="body" class="form-control" aria-label="With textarea" placeholder="Enter text" rows="10"></textarea>
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
            </div>
        </div>
    </div>
</template>

<script>
      import Axios from 'axios';
      import ErrorsFormater from '../services/errorsFormater';
      import Auth from '../services/auth';

      const errorsFormater = new ErrorsFormater();

      export default {
          name: "contact_message.vue",
          data() {
              return {
                  errors: [],
                  title: null,
                  body: null,
                  sended: false
              }
          },
          created() {
              Auth.checkToken(this.$router);
          },
          methods: {
              sendForm() {
                  const title = this.title;
                  const body = this.body;
                  Axios({
                      method: 'post',
                      url: 'api/contact-message/create',
                      data: {
                          title: title,
                          body: body
                      },
                      headers: Auth.getAuthorizationHeader()
                  }).then((response) => {
                      this.sended = true;
                      this.returnToForm();
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
              },
              returnToForm() {
                  this.errors = [];
                  setTimeout(() => this.sended = false, 2000);
            }
          },

      }
</script>