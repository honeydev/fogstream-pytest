<template>
    <div class="container">
        <div class="row">
            <div class="col-4 offset-4" style="margin-top: 10%">
    <form v-on:submit.prevent="sendForm()">
      <ul v-if="errors" class="error-messages list-unstyled">
            <li v-for="error in errors" class="alert alert-danger" role="alert">{{ error }}</li>
      </ul>
      <div class="form-group">
        <label for="exampleInputEmail1">Username</label>
        <input v-model="username" type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Username">
      </div>
        <div class="form-group">
        <label for="exampleInputEmail1">Email</label>
        <input v-model="email" type="text" class="form-control" id="" aria-describedby="emailHelp" placeholder="Enter email">
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input v-model="password" type="password" class="form-control" id="password" placeholder="Password">
      </div>
        <div class="form-group">
        <label for="passwordRepeat">Password repeat</label>
        <input v-model="passwordRepeat" type="password" class="form-control" id="passwordRepeat" placeholder="Password repeat">
      </div>
      <button class="btn btn-primary">Submit</button>
    </form>
            </div>
        </div>
    </div>
</template>

<script>
    import Axios from 'axios';
    import ErrorsFormater from '../services/errorsFormater';

    const errorsFormater = new ErrorsFormater();

    export default {
        name: "register",
        data() {
            return {
                errors: [],
                username: null,
                email: null,
                password: null,
                passwordRepeat: null
            }
        },
        methods: {
            sendForm() {
                const username = this.username;
                const email = this.email;
                const password = this.password;
                const passwordRepeat = this.passwordRepeat
                Axios.post('/api/register', {
                    username: username,
                    email: email,
                    password: password,
                    password_repeat: passwordRepeat
                }).then((response) => {
                    this.$router.push({ name: "login" })
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
        }
    }
</script>
