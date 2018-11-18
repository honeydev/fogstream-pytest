import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
      {
          name: "index",
          path: "/",
          component: () => import("./views/index.vue"),
      },
      {
          name: "login",
          path: "/login",
          component: () => import("./views/login.vue"),
      },
      {
          name: "register",
          path: "/register",
          component: () => import("./views/register.vue"),
      },
      {
          name: "contact-message",
          path: "/contact-message",
          component: () => import("./views/contact_message.vue"),
      },
  ]
});
