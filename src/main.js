import Vue from "vue";
import App from "./App.vue";
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import VueRouter from 'vue-router'
import Routes from './routes'
import VueVideoPlayer from 'vue-video-player'
import 'video.js/dist/video-js.css'
import PerfectScrollbar from 'vue2-perfect-scrollbar'
import 'vue2-perfect-scrollbar/dist/vue2-perfect-scrollbar.css'

// Font Awesome icons. Usage: https://buefy.org/documentation/icon/#custom-icon-pack , specify `pack` as "fas"
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

Vue.use(VueVideoPlayer)

Vue.use(PerfectScrollbar)

Vue.config.productionTip = false;

const router = new VueRouter({
  routes: Routes,
  mode: 'history'
})

new Vue({
  render: (h) => h(App),
  router: router
}).$mount("#app");
