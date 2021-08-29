import Vue from "vue";
import App from "./App.vue";
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import VueRouter from 'vue-router'
import Routes from './routes'

Vue.use(Buefy)
Vue.use(VueRouter)

Vue.config.productionTip = false;

const router = new VueRouter({
  routes: Routes,
  mode: 'history'
})

new Vue({
  render: (h) => h(App),
  router: router
}).$mount("#app");
