import Vue from "vue";
import App from "./App.vue";
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import VueRouter from 'vue-router'
import Routes from './routes'

// FA, add icons you need to the library
import { library } from '@fortawesome/fontawesome-svg-core';
import { fas } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
library.add(fas);
Vue.component('vue-fontawesome', FontAwesomeIcon);


Vue.use(Buefy, {
  defaultIconComponent: "vue-fontawesome",
  defaultIconPack: "fas",
  customIconPacks: {
    fas: {
      sizes: {
        default: "lg",
        "is-small": "1x",
        "is-medium": "2x",
        "is-large": "3x"
      },
      iconPrefix: ""
    }
  }
})

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
