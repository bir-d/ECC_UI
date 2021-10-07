<template>
    <div>
        <div class="columns">
            <div class="column is-half">
                <div class="video-wall">
                    <div class="upload">
                        <input type="file" @change="onFileChange">
                    </div>
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
                <div class="tags">
                    <span v-for="(file, index) in dropFiles" :key="index" class="tag is-primary">
                        {{file.name}}
                        <button class="delete is-small" type="button" @click="deleteDropFile(index)"></button>
                    </span>
                </div>
            </div>
            <div class="column is-narrow">
                <section class="media-wall files">
                    <h1 class="title">File Browser</h1>
                    <div class="columns">
                        <div class="column">
                            <figure class="image is-128x128">
                            <b-icon pack="fas" icon="file-video" size="is-large"></b-icon>
                            <p class="filename"> filename </p>
                            </figure>
                        </div>
                        <div class="column">
                            <figure class="image is-128x128">
                            <b-icon pack="fas" icon="file-video" size="is-large"></b-icon>
                            <p class="filename"> filename </p>
                            </figure>
                        </div>
                        <div class="column">
                            <figure class="image is-128x128">
                            <b-icon pack="fas" icon="file-video" size="is-large"></b-icon>
                            <p class="filename"> filename </p>
                            </figure>
                        </div>
                        <div class="column">
                            <figure class="image is-128x128">
                            <b-icon pack="fas" icon="file-video" size="is-large"></b-icon>
                            <p class="filename"> filename </p>
                            </figure>
                        </div>
                    </div>
                    <div class="columns">
                        <div class="column">
                            <figure class="image is-128x128">
                            <b-icon pack="fas" icon="file-video" size="is-large"></b-icon>
                            <p class="filename"> filename </p>
                            </figure>
                        </div>
                        <div class="column">
                            <figure class="image is-128x128">
                            <b-icon pack="fas" icon="file-video" size="is-large"></b-icon>
                            <p class="filename"> filename </p>
                            </figure>
                        </div>
                        <div class="column">
                            <figure class="image is-128x128">
                            <b-icon pack="fas" icon="file-video" size="is-large"></b-icon>
                            <p class="filename"> filename </p>
                            </figure>
                        </div>
                        <div class="column">
                            <figure class="image is-128x128">
                            <b-icon pack="fas" icon="file-video" size="is-large"></b-icon>
                            <p class="filename"> filename </p>
                            </figure>
                        </div>
                    </div>
                    <div class="columns">
                        <div class="column">
                            <figure class="image is-128x128">
                            <b-icon pack="fas" icon="file-video" size="is-large"></b-icon>
                            <p class="filename"> filename </p>
                            </figure>
                        </div>
                        <div class="column">
                            <figure class="image is-128x128">
                            <b-icon pack="fas" icon="file-video" size="is-large"></b-icon>
                            <p class="filename"> filename </p>
                            </figure>
                        </div>
                        <div class="column">
                            <figure class="image is-128x128">
                            <b-icon pack="fas" icon="file-video" size="is-large"></b-icon>
                            <p class="filename"> filename </p>
                            </figure>
                        </div>
                        <div class="column">
                            <figure class="image is-128x128">
                            <b-icon pack="fas" icon="file-video" size="is-large"></b-icon>
                            <p class="filename"> filename </p>
                            </figure>
                        </div>
                    </div>
                    <div class="columns">
                        <div class="column">
                            <figure class="image is-128x128">
                            <b-icon pack="fas" icon="file-video" size="is-large"></b-icon>
                            <p class="filename"> filename </p>
                            </figure>
                        </div>
                        <div class="column">
                            <figure class="image is-128x128">
                            <b-icon pack="fas" icon="file-video" size="is-large"></b-icon>
                            <p class="filename"> filename </p>
                            </figure>
                        </div>
                        <div class="column">
                            <figure class="image is-128x128">
                            <b-icon pack="fas" icon="file-video" size="is-large"></b-icon>
                            <p class="filename"> filename </p>
                            </figure>
                        </div>
                        <div class="column">
                            <figure class="image is-128x128">
                            <b-icon pack="fas" icon="file-video" size="is-large"></b-icon>
                            <p class="filename"> filename </p>
                            </figure>
                        </div>
                    </div>
                </section>
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
.upload{
    margin-bottom: 2.5em;
}
.video-player{
    width: 100%;
    height: 20%;
}
.wall-piece{
    margin-left: 1em;
}
.media-wall{
    height:100%;
    display: flex;
    overflow-y: auto;
    flex-direction: column;
    margin-top: 3em;
    margin-left: 7em;
}
.filename{
    opacity: 75%;
}
.files{
    border-radius: 5px;
    /* RGB "fake transparency" will be used by browsers which dont support rgba's "real transparency" */
    border-color: rgb(183, 183, 183);
    border-color: rgba(0, 0, 0, .5);
}
</style>

<script>
import 'video.js/dist/video-js.css'
import { videoPlayer } from 'vue-video-player'

export default {
  data() {
    return {
      file: {},
      dropFiles: [
          {
              label: String,
              address: String
          }
      ],
      playerOptions: {
          height: '360',
          autoplay: true,
          muted: true,
          language: 'en',
          playbackRates: [0.7, 1.0, 1.5, 2.0],
          sources: [{
            type: "video/mp4",
            src: "http://vjs.zencdn.net/v/oceans.mp4",
            }],
        }
      }
    },
  components:{
      videoPlayer
  },
  mounted() {
      // console.log('this is current player instance object', this.player)
      setTimeout(() => {
        console.log('dynamic change options', this.player)
        this.player.muted(false)
      }, 5000)
    },
  computed: {
      player() {
        return this.$refs.videoPlayer.player
      }
    },
  methods: {
    deleteDropFile(index) {
      this.dropFiles.splice(index, 1);
    },
      // player is ready
      playerReadied(player) {
        // seek to 10s
        console.log('example player 1 readied', player)
        player.currentTime(10)
      }
  }
};
</script>
