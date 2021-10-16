import homepage from './components/home-page.vue'
import videowall from './components/video-wall.vue'
import lightspage from './components/light-page.vue'
import displays from './components/display'
import workstation from './components/workstation.vue'

export default[
    {path:'/', component: homepage, name:"home"},
    {path:'/videowall', component: videowall},
    {path:'/lights', component: lightspage},
    {path:'/display',component: displays},
    {path:'/workstation',component: workstation}
]