import homepage from './components/home-page.vue'
import videowall from './components/video-wall.vue'
import lightspage from './components/light-page.vue'

export default[
    {path:'/', component: homepage},
    {path:'/videowall', component: videowall},
    {path:'/lights', component: lightspage}
]