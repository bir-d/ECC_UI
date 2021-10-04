import homepage from './components/home-page.vue'
import videowall from './components/video-wall.vue'
import lightspage from './components/light-page.vue'
import displays from './components/display'
import tests from './components/test.vue'
import tests2 from './components/test2.vue'

export default[
    {path:'/', component: homepage},
    {path:'/videowall', component: videowall},
    {path:'/lights', component: lightspage},
    {path:'/display',component: displays},
    {path:'/test',component: tests},
    {path:'/test2',component: tests2}
]