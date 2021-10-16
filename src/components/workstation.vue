<template>
    <div>
        <div class="columns is-desktop">
            <div class="column">
                <div class="video-wall" v-for="station in workstations" :key="station" >
                    <h1 id="heading" v-on:click="toggleSelected(station)"> Workstation {{station.id}} </h1>
                    <div class="item" v-bind:class="[station.selected ? 'selected2' : '']">
                        <div class="player" >
                        <video-player  class="vjs-custom-skin"
                                        ref="videoPlayer"
                                        :options="station.playerOptions"
                                        :playsinline="true"
                                        @play="onPlayerPlay($event)"
                                        @pause="onPlayerPause($event)"
                                        @ended="onPlayerEnded($event)"
                                        @loadeddata="onPlayerLoadeddata($event)"
                                        @waiting="onPlayerWaiting($event)"
                                        @playing="onPlayerPlaying($event)"
                                        @timeupdate="onPlayerTimeupdate($event)"
                                        @canplay="onPlayerCanplay($event)"
                                        @canplaythrough="onPlayerCanplaythrough($event)"
                                        @ready="playerReadied"
                                        @statechanged="playerStateChanged($event)">
                        </video-player>
                        </div>
                    </div>
                </div>
                
                
            </div>
            <div class="column">
                <h1 class="title">File Browser</h1>
                <perfect-scrollbar>
                    <div class="columns is-multiline">
                        <div class="column is-one-third"
                        v-for="(element) in media" 
                        :key="element">
                            <button @click="load(element.id)">
                            <figure class="image is-128x128">
                            <b-icon pack="fas" icon="file-video" size="is-large"></b-icon>
                            <p class="filename"> {{ element.name }}</p>
                            </figure>
                            </button>
                        </div>
                    </div>
                </perfect-scrollbar>
            </div>
        </div>
    </div>
</template>

<style scoped>
.title{
    margin-top: 1em;
    margin-bottom: 1.5em;
}
.video-wall{
    margin-top: 3em;
    margin-left: 2.5em;
}
.filename{
    opacity: 75%;
}
/* Controls the video player dimensions */
.ps {
  height: 600px;
}
#heading {
    font-size:2cm;
    text-align:left;
}
.selected2 {
    border: 5px solid red;
}
</style>

<script>
import 'video.js/dist/video-js.css'
import axios from 'axios'
import { videoPlayer } from 'vue-video-player'
import { PerfectScrollbar } from 'vue2-perfect-scrollbar'

export default {
    data() {
        return {
        // Media information stored here
        media: [
            {id:0, label:"Seaside1", type: "video/mp4", src: "http://vjs.zencdn.net/v/oceans.mp4"},
            {id:1, label:"Boat Ride2", type: "video/mp4", src: "https://cdn.theguardian.tv/webM/2015/07/20/150716YesMen_synd_768k_vp8.webm"},
            ],
        workstations: [
            {
                id: 1,
                selected: false,
                // Functionality for the video player 
                playerOptions: {
                    height: '360',
                    width: '540',
                    autoplay: false,
                    muted: true,
                    language: 'en',
                    playbackRates: [0.7, 1.0, 1.5, 2.0],
                    sources: [],
                }
            },
            {
                id: 2,
                selected: false,
                playerOptions: {
                    height: '360',
                    width: '540',
                    autoplay: false,
                    muted: true,
                    language: 'en',
                    playbackRates: [0.7, 1.0, 1.5, 2.0],
                    sources: [],
                }
            },
            {
                id: 3,
                selected: false,
                playerOptions: {
                    height: '360',
                    width: '540',
                    autoplay: false,
                    muted: true,
                    language: 'en',
                    playbackRates: [0.7, 1.0, 1.5, 2.0],
                    sources: [],
                }
            },
        ],
        }
    },
    components:{
        videoPlayer,
        PerfectScrollbar
    },
    computed: {
        player() {
            return this.$refs.videoPlayer.player
        }
    },
    mounted() {
        setTimeout(() => {
            this.player.muted(false)
        }, 5000)
    },
    created() {
        //this.getMedia();
    },
    methods: {
        toggleSelected: function(Selectedstation) {
                //Inverts the value of 'light.selected' (true -> false, false -> true)
                Selectedstation.selected = !Selectedstation.selected
            },
        // Ensure Video Player is ready
        playerReadied(player) {
            // seek to 10s
            console.log('example player 1 readied', player)
            player.currentTime(10)
        },
        // Load the videos into Source list
        load(id){
            for(this.element in this.workstations) {
                if(this.element.selected == true) {
                    this.element.playerOptions.sources.unshift({
                    label: this.media[id].label, 
                    id: this.media[id].id, 
                    type: this.media[id].type, 
                    src: this.media[id].src})

                }

            }
        },
        getWorkStations() {
            axios({
                method:'get',
                // Url of backend location of data
                url: 'http://127.0.0.1:8000/api/workstations/',
                auth: {
                    username: 'admin',
                    password: 'eccadmin123'
                }
            
            }).then((response) => {

                this.isLoaded = true;

                // Check the response was a success
                if(response.data != 'undefined')
                {
                    this.workstations = response.data;
                    // Calls function to update lights values with db values
                    //this.updateLights();
                }
            });
            },
        getMedia() {
            axios({
                method:'get',
                // Url of backend location of data
                url: 'http://127.0.0.1:8000/api/videowall/',
                auth: {
                    username: 'admin',
                    password: 'eccadmin123'
                }
            // This section tells code to wait until lights have been rendered to extract db lights info
            }).then((response) => {

                this.isLoaded = true;

                // Check the response was a success
                if(response.data != 'undefined')
                {
                    this.mediasrc = response.data;
                    // Calls function to update media list with db values
                    this.updateMedia();
                }
            });
        },
        updateMedia() {
            for (this.vuemedia in this.media) {
                for (this.djangomedia in this.dbmedia) {
                    if(this.media[this.vuemedia].label == this.dbmedia[this.djangomedia].name) {
                        this.media[this.vuemedia].label = this.dbmedia[this.djangomedia].name
                        this.media[this.vuemedia].id = this.dbmedia[this.djangomedia].id
                        this.media[this.vuemedia].type = this.dbmedia[this.djangomedia].type
                        this.media[this.vuemedia].src = this.dbmedia[this.djangomedia].src
                    }
                }
            }
        },
        
    }
};
</script>
