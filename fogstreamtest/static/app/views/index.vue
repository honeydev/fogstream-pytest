<template>
     <div>
     <div class="container">
          <nav>
               <a href="/admin">Admin Login</a>
          </nav>
     </div>
     <div class="container" style="margin-top: 20%">
          <div class="row d-flex h-100">
               <div class="mx-auto my-auto">
                    <nav>
                         <router-link :to="{name: 'login'}">Sign in</router-link>
                         or
                         <router-link :to="{name: 'register'}">Register</router-link>

                    </nav>
               </div>
          </div>
     </div>
     </div>
</template>
<script>

    import login from './login.vue'
    import register from './register.vue'
    import contactMessage from './contact_message.vue'
    import Auth from '../services/auth';

    export default {
        name: "index",
        data() {
            return {
                authorized: false
            }
        },
        created() {
            Auth.checkAuth(this)
        },
        watch: {
            authorized() {
                if (this.authorized) {
                    this.$router.push({ name: "contact-message" })
                }
            }

        }
    }
</script>
