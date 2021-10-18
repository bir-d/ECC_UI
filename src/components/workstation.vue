<template>
    <div v-if="workstationsplayer[0].id != 'undef'">
        <div class="columns is-desktop">
            <div class="column is-7">
                <!-- A workstation is rendered for each workstation in db -->
                <div class="workstation" v-for="station in workstationsplayer" :key="station" >
                    <h1 class="is-family-sans-serif has-text-weight-normal" id="heading" v-on:click="toggleSelected(station)"> Workstation {{station.id}} </h1>
                    <div class="item" v-bind:class="[station.selected ? 'selected2' : '']">
                        <div class="player" >
                            <!-- Video Player for Workstation -->
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
                <div class="file_browser">
                    <!-- Infinite scroll on media in projewct -->
                <perfect-scrollbar>
                    <div class="columns is-multiline">
                        <div class="column is-one-third"
                        v-for="(element) in media" 
                        :key="element">
                            <button @click="load(element.id)">
                            <figure class="image">
                                <b-icon pack="fas" icon="play-circle" size="is-large"></b-icon>
                                <p class="filename is-size-2 is-family-sans-serif"> {{ element.label }}</p>
                            </figure>
                            </button>
                        </div>
                    </div>
                </perfect-scrollbar>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.title{
    margin-top: 1em;
    margin-bottom: 1.5em;
}
.workstation{
    margin-top: 3em;
    margin-left: 2.5em;
}
.filename{
    opacity: 75%;
}
#heading {
    font-size:2cm;
    text-align:left;
}
.selected2 {
    border: 5px solid red;
}
.file_browser{
    margin-top: 10em;
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
        workstations: [],
        workstationsplayer: [],
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
        this.getWorkStations()
        setTimeout(() => {
            this.player.muted(false)
        }, 5000)
        
    },
    created() {
        this.getMedia();
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
            for(let i = 0; i < this.workstationsplayer.length; i++){
                
                if(this.workstationsplayer[i].selected == true) {
                    this.workstationsplayer[i].playerOptions.sources.unshift({
                    label: this.media[id].label, 
                    id: this.media[id].id, 
                    type: this.media[id].type, 
                    src: this.media[id].src})
                    this.workstationsplayer[i].selected = false
                    this.workstationsplayer[i].source = this.media[id].src
                    this.workstationsplayer[i].media_name = this.media[id].label
                    this.workstationsplayer[i].media_type = this.media[id].type
                    // Update db with selected media
                    axios({
                        method:'put',
                        url: 'http://127.0.0.1:8000/api/workstations/' + this.workstationsplayer[i].id,
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        data: {
                            id: this.workstationsplayer[i].id,
                            source: this.workstationsplayer[i].source,
                            media_name: this.workstationsplayer[i].media_name,
                            media_type: this.workstationsplayer[i].media_type,
                            station_on: this.workstationsplayer[i].station_on,
                            workstation_name: this.workstationsplayer[i].workstation_name,
                        },
                        auth: {
                            username: 'admin',
                            password: 'eccadmin123'
                        }
                        })

                }

            }
        },
        //Mesh workstation db values with player option values
        WorkstationMesh() {
            for(let i = 0; i < this.workstations.length; i++){
                var PlayOp = {}
                if(this.workstations[i].media_name != 'example') {
                    PlayOp = {height: '360',
                    width: '540',
                    autoplay: false,
                    muted: true,
                    language: 'en',
                    playbackRates: [0.7, 1.0, 1.5, 2.0],
                    sources: [{label: this.workstations[i].media_name, src: this.workstations[i].source, type: this.workstations[i].media_type}]
                    }
                }
                else {
                    PlayOp = {height: '360',
                    width: '540',
                    autoplay: false,
                    muted: true,
                    language: 'en',
                    playbackRates: [0.7, 1.0, 1.5, 2.0],
                    sources: []
                    }

                }
                
                let station = {'id': this.workstations[i].id, 'media_name': this.workstations[i].media_name, 'media_type': this.workstations[i].media_type, 'source': this.workstations[i].source, 'station_on': this.workstations[i].station_on, 'workstation_name': this.workstations[i].workstation_name, 'selected': false, 'playerOptions': PlayOp}
                this.workstationsplayer.push(station)
            }
        },
        // Load Workstations from db
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
                    this.WorkstationMesh()
                    
                }
            });
            },
        getMedia() {
            axios({
                method:'get',
                // Url of backend location of data
                url: 'http://127.0.0.1:8000/api/video_wall/',
                auth: {
                    username: 'admin',
                    password: 'eccadmin123'
                }
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
