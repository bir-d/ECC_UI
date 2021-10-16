<template>
    <div>
        <div class="columns is-desktop">
            <div class="column is-7">
                <div class="video-wall">
                    <div class="item">
                        <div class="player">
                        <video-player  class="vjs-custom-skin"
                                        ref="videoPlayer"
                                        :options="playerOptions"
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
                <h1 class="title is-size-1 is-family-sans-serif	has-text-weight-medium">File Browser</h1>
                <perfect-scrollbar>
                    <div class="columns is-multiline">
                        <div class="column is-one-third"
                             v-for="(element) in media" 
                             :key="element">
                            <button @click="load(element.id)">
                            <div class="box">
                                <b-icon pack="fas" icon="play-circle" size="is-large"></b-icon>
                                <p class="filename is-size-2 is-family-sans-serif"> {{ element.label }}</p>
                            </div>
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
            {
                id:0, 
                label:"Seaside1", 
                type: "video/mp4", 
                src: "http://vjs.zencdn.net/v/oceans.mp4",
                selected: true
            },
            {
                id:1, 
                label:"Boat Ride2", 
                type: "video/mp4", 
                src: "https://cdn.theguardian.tv/webM/2015/07/20/150716YesMen_synd_768k_vp8.webm",
                selected: true
            },
        ],
        // Functionality for the video player 
        playerOptions: {
            height: '360',
            autoplay: true,
            muted: true,
            language: 'en',
            playbackRates: [0.7, 1.0, 1.5, 2.0],
            notSupportedMessage: 'This video is not able to play',
            aspectRatio: '16:9',
            poster: '',
            nativeControlsForTouch: true,
            sources: [],
            }
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
        this.getMedia();
    },
    methods: {
        // Ensure Video Player is ready
        playerReadied(player) {
            // seek to 10s
            console.log('example player 1 readied', player)
            player.currentTime(10)
        },
        // Load the videos into Source list
        load(id){
            this.playerOptions.sources.unshift({
                label: this.media[id].label, 
                id: this.media[id].id, 
                type: this.media[id].type, 
                src: this.media[id].src,
                selected: this.media[id].selected,
                })
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
                    if(this.media[this.vuemedia].label == this.dbmedia[this.djangomedia].media_name) {
                        this.media[this.vuemedia].label = this.dbmedia[this.djangomedia].media_name
                        this.media[this.vuemedia].id = this.dbmedia[this.djangomedia].id
                        this.media[this.vuemedia].type = this.dbmedia[this.djangomedia].media_type
                        this.media[this.vuemedia].src = this.dbmedia[this.djangomedia].source
                        this.media[this.vuemedia].selected = this.dbmedia[this.djangomedia].selected
                    }
                }
            }
        },
        // Adds array to presets array that contains info for storing preset
        AddPreset: function(PresetName){
            this.presets.push({
                name: PresetName,
                presetinfo: [ {
                    label: this.playerOptions.sources[0].label,
                    id: this.playerOptions.sources[0].id,
                    type: this.playerOptions.sources[0].type,
                    src: this.playerOptions.sources[0].src,
                    selected: this.playerOptions.sources[0].selected,
                }
                ]
            })
            this.newPresetName = ''
            },
            // loops through presets, for preset with inputted name and updates all lights with their preset values
            SyncPresets: function(PresetName){
                for (this.element in this.presets) {
                    if (this.presets[this.element].name == PresetName) {
                        for (this.presetconfig in this.presets[this.element].presetinfo) {
                            for (this.mediaconfig in this.media) {
                                if (this.presets[this.element].presetinfo[this.presetconfig].label == this.playerOptions.sources[this.mediaconfig].label) {
                                    this.playerOptions.sources[this.mediaconfig].label = this.presets[this.element].presetinfo[this.presetconfig].label
                                    this.playerOptions.sources[this.mediaconfig].id = this.presets[this.element].presetinfo[this.presetconfig].id
                                    this.playerOptions.sources[this.mediaconfig].type = this.presets[this.element].presetinfo[this.presetconfig].type
                                    this.playerOptions.sources[this.mediaconfig].src = this.presets[this.element].presetinfo[this.presetconfig].src
                                    this.playerOptions.sources[this.mediaconfig].selected = this.presets[this.element].presetinfo[this.presetconfig].selected
                                }
                            }
                        }
                    }
                }
                this.PresetName = '';
            }
    }
};
</script>
