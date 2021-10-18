<template>
  <div class="content">
    <div class = "columns">
      <div class="column is-three-fifths">
      <div class="screens">
          <!--    the screen 1 at the left side    -->
          <h1 class="is-size-1">Screen 1</h1>
          <div class='screen1Left'>
            <video-player class="video-player vjs-custom-skin"
                          ref="videoPlayer"
                          :playsinline="true"
                          :options="playerOptions">
            </video-player>
          </div>

          <!--        the screen two at the left side-->
          <h1 class="is-size-1">Screen2</h1>
          <div class='screen2Left'>
            <video-player class="video-player vjs-custom-skin"
                          ref="videoPlayer"
                          :playsinline="true"
                          :options="playerOptions2"
            >
            </video-player>
          </div>
        </div>
      </div>


    <div class="column">
<!-- a section to store the videos information from  the DB-->
      <section>
        <button
            class="fontSize button is-info is-light is-fullwidth has-text-weight-bold is-size-3"
            @click="isActive = !isActive"> File Browser</button>
                <b-notification v-model="isActive" aria-close-label="Close notification">
                  <ul>
                    <li v-for ="item in displayPreset"
                        :key = "item.id" class = 'fontSize'>
                      {{ 'ID:  '+ item.id+ ","  }}
                      {{ 'Name: '+item.media_name }}
                    </li>
                  </ul>
                </b-notification>

      </section>

<!--      // the video to be displayed in Screen1 from DB-->

      <div>

<!--        allow the user to select the video to display in screen base on the ID-->
        <div class = 'half'>
        <div class="field is-horizontal" id="url">
            <div class="field-label is-large">
              <label class="label is-size-3 has-text-left">Screen1: </label>
            </div>
            <div class="field-body">
              <div class="field">
                <input class="input is-rounded is-large"
               placeholder="type the ID of videos"
               type="text"
               v-model="screen1Id"
               >
              </div>
            <button id="load"
                  class="button is-large is-rounded is-success is-light has-text-weight-medium"
                  @click="loadScreen1">Load</button>
            </div>
          </div>


<!--       the video to be displayed in Screen2 from DB -->
      <div class="field is-horizontal" id="url">
            <div class="field-label is-large">
              <label class="label is-size-3 has-text-left">Screen2: </label>
            </div>
            <div class="field-body">
              <div class="field">
                <input class="input is-rounded is-large"
                 placeholder="type the ID of videos"
                 type="text"
                 v-model="screen2Id"
                 >
              </div>
            <button id="load" class="button is-large is-rounded is-danger is-light has-text-weight-medium"
                  @click="loadScreen2">Load</button>
            </div>
          </div>
        </div>
      </div>
      <div class="input_fields">


<!--           Ask the User for the Url of the videl-->
          <div class="field is-horizontal" id="url">
            <div class="field-label is-large">
              <label class="label is-size-3 has-text-left">URL: </label>
            </div>
            <div class="field-body">
              <div class="field">
                <input class="input is-rounded is-large"
                       type="text" v-model="urlData"
                placeholder="Or display the video with correct Url">
              </div>
            </div>
          </div>
      </div>


<!--two button indicate the two screens, click the button will change the video in the screen with the URl from user-->
        <div class="screen_select">
          <button class="button is-rounded is-success is-light is-large has-text-weight-medium"
                  @click="clickScreen1(); "
                  type="is-primary is-light"
                  id="screen_1">Screen 1
          </button>
          <button class="button is-rounded is-danger is-light is-large has-text-weight-medium"
                  @click="clickScreen2(); "
                  type="is-success is-light"
                  id="screen_2">Screen 2
          </button>
        </div>
      </div>
    </div>
  </div>

</template>

<style scoped>
.content, .screen_select, #url{
  margin-top: 3.5em;
}
.screens{
  margin-left: 3.5em;
  margin-right: 3.5em;
}
.input_fields{
  margin-top: 5em;
  margin-left: 2em;
  margin-right: 5em;
}
#screen_1{
  margin-right:3.5em;
}
/*display the content in the middle*/
.fontSize{
  font-size:20px;
}

</style>

<script>
import axios from 'axios'

export default {


  data() {
    return {


      playerOptions: {
        playbackRates: [0.5, 1.0, 1.5, 2.0], // play speed
        autoplay: false,
        muted: false,
        loop: false,      // restart the video or not
        preload: 'auto',  // set to auto, check by the browser.
        language: 'zh-CN',
        aspectRatio: '16:9',
        fluid: true,  // when is true，Video.js player  will self-adapt the window size
        sources: [{
          type: "video/mp4",  // type
          // url location
          src: "https://media.w3.org/2010/05/sintel/trailer.mp4",
          // src: ''   dynamically bind the value from db , need update from the DB
        }],
        poster: '',
        notSupportedMessage: 'This video is not able to play',  // display when video is not able to play
        controlBar: {
          timeDivider: true,           // divider for current time and remaining time
          durationDisplay: true,
          remainingTimeDisplay: false, // display the remaining time or not
          fullscreenToggle: true       // full screen button
        },

      },
      playerOptions2: {
        playbackRates: [0.5, 1.0, 1.5, 2.0], // play speed
        autoplay: false,
        muted: false,
        loop: false,      // restart the video or not
        preload: 'auto',  // set to auto, check by the browser.
        language: 'zh-CN',
        aspectRatio: '16:9',
        fluid: true,  // when it is true，Video.js player  will self-adapt the window size
        sources: [{
          type: "video/mp4",
          // url
          src: "http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4",
          // src: ''   dynamically bind the value from db , need update from the DB

        }],
        poster: '',
        notSupportedMessage: 'This video is not able to play',  // display when video is not able to play
        controlBar: {
          timeDivider: true,           // divider for current time and remaining time
          durationDisplay: true,
          remainingTimeDisplay: false, // display the remaining time or not
          fullscreenToggle: true       // full screen button
        },

      },

      // data stored from the API
      displayPreset: [],


      // the Url information from the user
      urlData: '',


      //  the screen1 Id from the user
      screen1Id: '',
      screen2Id: '',

      // change the activity of the button that show media information
      isActive: true,

      // the video List
      productList: []
    }


  },
  created() {
    this.getData()
  },
  methods: {
    // ask for data from the DB
    getData() {
      axios({
        method: 'get',
        // Url of backend location of data
        url: 'http://127.0.0.1:8000/api/media',
        auth: {
          username: 'admin',
          password: 'eccadmin123'
        }
      }).then((response) => {
        this.displayPreset = response.data
        this.numPreset = this.displayPreset.length
        // bind the value of two screens after reading the value

        this.playerOptions.sources[0].src = this.displayPreset[0].source
        this.playerOptions2.sources[0].src = this.displayPreset[1].source

      });
    },



    // loading the video with the Url from the User,
    clickScreen1: function () {
//      check the format of Url
// eslint-disable-next-line
      let reUrl01 = /^((ht|f)tps?):\/\/([\w-]+(\.[\w-]+)*\/?)+(\?([\w\-\.,@?^=%&:\/~\+#]*)+)?$/;

      if ((this.urlData === '') || (reUrl01.test(this.urlData) == false)) {
        this.$buefy.notification.open('please provide the correct Url of video')
        return
      }
      this.$buefy.notification.open('reload the screen1 with the new src!, screen1 has been updated')
      this.playerOptions.sources[0].src = this.urlData
    },


    clickScreen2() {
      // eslint-disable-next-line
      let reUrl01 = /^((ht|f)tps?):\/\/([\w-]+(\.[\w-]+)*\/?)+(\?([\w\-\.,@?^=%&:\/~\+#]*)+)?$/;
      if ((this.urlData === '') || (reUrl01.test(this.urlData) == false)) {
        this.$buefy.notification.open('please provide the correct Url of video')
        return
      }
      this.$buefy.notification.open('reload the screen2 with the new src!, screen2 has been updated')
      this.playerOptions2.sources[0].src = this.urlData
    },


    // clear the url in the UrlData( from User)
    clearUrl() {
      this.urlData = ''
      // this.
    },

    // reload the video base on the Id
    loadScreen1() {

      if ((this.screen1Id > this.displayPreset.length) || (this.screen1Id == 0)) {
        // window.alert('please select a valid video Id')
        this.$buefy.notification.open('please select a valid video Id for screen1')
        return
      }
      this.playerOptions.sources[0].src = this.displayPreset[this.screen1Id - 1].source

    },
    loadScreen2() {
      if ((this.screen2Id > this.displayPreset.length) || (this.screen2Id == 0)) {
        // window.alert('please select a valid video Id')
        this.$buefy.notification.open('please select a valid video Id for screen2')
        return
      }
      this.playerOptions2.sources[0].src = this.displayPreset[this.screen2Id - 1].source

    },


  }
}



</script>
