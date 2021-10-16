<template>
  <div class="content">
    <div class = 'left'>
      <section>
<!--         ask the user which preset should be load-->
        <div>
        <h5 class = 'moveLeft'> Preset </h5>
        <select  class = 'moveLeft' v-model="PresettActive" placeholder="Select a preset" @change="changePreset($event)" >
          <option v-for="(item,index) in productList" :key="index" :value='item.id'>{{item.title}}</option>
        </select>
    
<!--          a button allow the user to change preset-->
          <b-button type="is-info is-light" class = 'moveLeft' @click="loadPreset">Loading</b-button>

        </div>



        <!--    the screen 1 at the left side    -->
        <h1 id="screen1Title">Screen 1</h1>

        <div class='screen1Left'>
          <video-player class="video-player vjs-custom-skin"
                        ref="videoPlayer"
                        :playsinline="true"
                        :options="playerOptions"
          >
          </video-player>
        </div>

        <!--        the screen two at the left side-->
        <h1>Screen2</h1>
        <div class='screen2Left'>
          <video-player class="video-player vjs-custom-skin"
                        ref="videoPlayer"
                        :playsinline="true"
                        :options="playerOptions2"
          >
          </video-player>
        </div>
      </section>
    </div>

    <div class = 'right'>

      <div>
        <!--     ask the user , which preset is loaded in page-->
        <b-field label="type the Url of the video">

          <b-input v-model="urlData">
          </b-input>

        </b-field>
      </div>
        
      <div>
        <section>
<!--           a delete button allow the user to delete the Url-->
          <b-button type="is-warning is-light" @click="clearUrl">delete Url</b-button>

          <b-button
              label="Display the video"
              class="block"
              @click="isActive = !isActive" />
          <b-notification v-model="isActive" aria-close-label="Close notification">
            <h5>chose the screens you want to display the video</h5>
            <b-button @click="clickScreen1" type="is-primary is-light" >Screen1</b-button>
            <b-button @click="clickScreen2" type="is-success is-light">Screen2</b-button>
          </b-notification>
        </section>
      </div>
    </div>
  </div>

</template>




<style scoped>

.screen1Left{
  border-top: 2px solid darkred;
  margin-top: 1em;
  margin-bottom: 1.5em;
}

.screen2Left{
  /*margin-top: 200px;*/
  border-top: 2px solid darkred;
}
/* set the preset, and loaing button to the left*/
.moveLeft{
 float:left;
  width:100px;
}


/*contents of two screens*/
.content{
  height:1500px;
}
div.left {
  background-color:#eeeeee;
  width: 65%;
  height: 1500px;
  float: left;
}
.screens{
  margin-left: 3.5em;
  margin-right: 3.5em;
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
      displayPreset:[],


      // the Url information from the user
      urlData: '',


      // values in the selectors , if more presets are add in the database, this list should also be update to allow user to load new preset
      productList:[{id:1,title:"Test1"},{id:2,title:"Test2"},
        {id:3,title:"PresetNew1"},{id:4,title:"PresetNew2"},{id:5,title:"PresetNew3"}
      ],
      PresetActive:"1",// get the value of the Preset from user, default set as 1
    }
  },
  created(){
    this.getData()
  },
  methods: {
    // ask for data from the DB
    getData(){
      axios({
        method:'get',
        // Url of backend location of data
        // load the preset instead of the endpoint of display
        // url: 'http://127.0.0.1:8000/api/displays/',
        url: 'http://127.0.0.1:8000/api/preset/',
        auth: {
          username: 'admin',
          password: 'eccadmin123'
        }
        // This section tells code to wait until lights have been rendered to extract db lights info
      }).then((response) => {
        this.displayPreset = response.data

        // bind the value of these two when read the value
        // add the correct url for the display screens , and comment out the next two lines

        // this.playerOptions.sources[0].src = this.displayPreset[this.PresetActive].displays[0].source
        // this.playerOptions2.sources[0].src = this.displayPreset[this.PresetActive].displays[1].source

        // console.log('data',this.displayPreset)
        // console.log('media_src',this.displayPreset[this.PresetActive].displays[0].source)
        // console.log('media_sr2c',this.displayPreset[this.PresetActive].displays[1].source)

      });
    },

    // methods for loading the video and provide a url

    //pup up message when click the button
    clickScreen1() {
      if (this.urlData === '') return
      this.$buefy.notification.open('reload the screen1 with the new src!, screen1 has been updated')
      this.playerOptions.sources[0].src = this.urlData

      // console.log(this.presetNumber)
    },
    clickScreen2() {
      if (this.urlData === '') return
      this.$buefy.notification.open('reload the screen2 with the new src!, screen2 has been updated')
      this.playerOptions2.sources[0].src = this.urlData
    },

    //  dynamically select the value from selector
    changePreset(event) {
      this.PresetActive = event.target.value; // get the corresponding value in options
      // console.log("load preset",this.PresetActive)
    },

    // clear the url in the UrlData( from User)
    clearUrl(){
      this.urlData = ''
      // this.
    },

    // reload the video base on the Preset Num
    loadPreset(){
      axios({
        method:'get',
        // Url of backend location of data
        // load the preset instead of the endpoint of display
        // url: 'http://127.0.0.1:8000/api/displays/',
        url: 'http://127.0.0.1:8000/api/preset/',
        auth: {
          username: 'admin',
          password: 'eccadmin123'
        }
        // This section tells code to wait until lights have been rendered to extract db lights info
      }).then((response) => {
        this.displayPreset = response.data

        // bind the value of these two when read the value
        // add the correct url for the display screens , and comment out the next two lines

        // this.playerOptions.sources[0].src = this.displayPreset[this.PresetActive].displays[0].source
        // this.playerOptions2.sources[0].src = this.displayPreset[this.PresetActive].displays[1].source

        // console.log('data',this.displayPreset)
        // console.log('media_src',this.displayPreset[this.PresetActive].displays[0].source)
        // console.log('media_sr2c',this.displayPreset[this.PresetActive].displays[1].source)


      });
    },



  }
}
</script>
