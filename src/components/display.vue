<template>
  <div class="content">
    <div class = 'left'>
      <section>
        <!--    the screen 1 at the left side    -->
        <h1>Screen 1</h1>
<!--        load different preset?-->
<!--        <button >change video</button>-->


        <div class='screen1Left'>
          <video-player class="video-player vjs-custom-skin"
                        ref="videoPlayer"
                        :playsinline="true"
                        :options="playerOptions">
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

    <!--some preload img or video from the database?-->
    <div class = 'right'>

<!--allow the user to upload the video-->
<!--      <div>-->
<!--        <input type = 'file' accept = 'video/*' @change = 'loadFile'>-->
<!--        <video id="file" width="480" height="270" v-show="showVideo" controls/>-->
<!--      </div>-->
      <div>
<!--                // ask the user , which preset is loaded in page-->
                  <b-field label="type the Url of the video">
                    <b-input v-model="urlData"></b-input>
                </b-field>
      </div>

      <div>
        <section>
          <b-button
              label="Display the video"
              class="block"
              @click="isActive = !isActive" />
          <b-notification v-model="isActive" aria-close-label="Close notification">
            <span>chose the screens you want to display the video</span>
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
}
.screen2Left{
  /*margin-top: 200px;*/
  border-top: 2px solid darkred;
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
div.right {
  width: 35%;
  height:1000px;
  float: left;
}
/* a single grid for the img in the left side of screen 1*/
.grid1{
  margin:30px 35px;
}
/* img of three for one line*/
.imgBlock{
  width:100px;
  height: 150px;
  /*margin:0 50px;*/
  display:flex;
  flex-direction: row;
}
.screen1Right{
  margin-top: 15px;
  text-align: center;
}
.screen2Right{
  margin-top: 400px;
  text-align: center;
}


</style>




<script>
import axios from 'axios'
// import VueAxios from 'vue-axios'
// import { PerfectScrollbar } from 'vue2-perfect-scrollbar'

export default {


  data() {
    return {
      file: {},
      dropFiles: [],

      // toggoleActive
      isActive:true,

      //el
      // dialogImageUrl: '',
      // dialogVisible: false,
      disabled: false,

      playerOptions: {
        playbackRates: [0.5, 1.0, 1.5, 2.0], // play speed
        autoplay: false,
        muted: false,     // default set as false
        loop: false,      // restart the video or not
        preload: 'auto',  // set to auto, check by the browser.
        language: 'zh-CN',
        aspectRatio: '16:9',  // "16:9" or "4:3"）
        fluid: true,  // when is true，Video.js player  will self-adapt the window size
        sources: [{
          type: "video/mp4",  // type
          // url location
          src: 'http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4' ,
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
        muted: false,     // default set as false
        loop: false,      // restart the video or not
        preload: 'auto',  // set to auto, check by the browser.
        language: 'zh-CN',
        aspectRatio: '16:9',  // "16:9" or "4:3"）
        fluid: true,  // when it is true，Video.js player  will self-adapt the window size
        sources: [{
          type: "video/mp4",
          // url
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


      // data stored from the API
      displayPreset:[],

      // upload variable , video
      showImg:false,
      showVideo:false,

      // // save the url from the preset, bind the value with axios
      // screen1Url : '',
      // screen2Url : '',

      // the Url information from the user
      urlData: '',

      // the preset value from the user
      presetValue:'',
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
        url: 'http://127.0.0.1:8000/api/displays/',
        auth: {
          username: 'admin',
          password: 'eccadmin123'
        }
        // This section tells code to wait until lights have been rendered to extract db lights info
      }).then((response) => {
        this.displayPreset = response.data

        // bind the value of these two when read the value
        // src? not in the DB yet, add to the preset?
        // add the url for the display screesn, implement to a for loop if there are more file is the db
        this.playerOptions.sources[0].src = this.displayPreset[0].src
        this.playerOptions2.source[0].src = this.displayPreset[1].src

        console.log('data',this.displayPreset)
        console.log('media_name',this.displayPreset[0].media)


      });
    },

    // methods for loading the video and provide a url
    loadFile(event){
      const reader = new FileReader();
      const that = this
      if(!process.browser)return
      reader.onload = function(){
        const output = document.querySelector("#file")
        that.showVideo = true;
        output.src = URL.createObjectURL(new Blob([reader.result]))
        this.playerOptions2.sources[0].src = output.src

      }
      reader.readAsArrayBuffer(event.target.files[0])

    },

    //pup up message when click the button
    clickScreen1() {
      if (this.urlData === '') return
      this.$buefy.notification.open('reload the screen1 with the new src!, screen1 has been updated')
      this.playerOptions.sources[0].src = this.urlData
    },
    clickScreen2() {
      if (this.urlData === '') return
      this.$buefy.notification.open('reload the screen2 with the new src!, screen2 has been updated')
      this.playerOptions2.sources[0].src = this.urlData

    }


    }
}

</script>
