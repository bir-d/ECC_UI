<<template>
  <div class="content">
    <div class = 'left'>
      <section>
        <!--    the screen 1 at the left side    -->
        <h1>Screen 1</h1>
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
      <div>
        <h3 class = screen1Right>the images/videos for screen1</h3>
        <div class="imgBlock">
          <img src='https://picsum.photos/id/431/1230/500' alt ='img1' class='grid1'>
          <img src='https://picsum.photos/id/432/1230/500' alt ='img2' class='grid1'>
          <img src='https://picsum.photos/id/433/1230/500' alt ='img3' class='grid1'>
        </div>
        <div class="imgBlock">
          <img src='https://picsum.photos/id/434/1230/500' alt ='img4' class='grid1'>
          <img src='https://picsum.photos/id/435/1230/500' alt ='img5' class='grid1'>
          <img src='https://picsum.photos/id/436/1230/500' alt ='img6' class='grid1'>
        </div>
      </div>

      <div >
        <h3 class="screen2Right">the images/videos for screen2</h3>
        <div>
          <!--          the upload button for screen two, I use another UI framework, element UI for this task-->
          <el-upload
              action="#"
              list-type="picture-card"
              ref="upload"
              class="colorSetting"
              :auto-upload="false">
            <i slot="default" class="el-icon-plus"></i>
            <div slot="file" slot-scope="{file}">
              <img
                  class="el-upload-list__item-thumbnail"
                  :src="file.url" alt=""
              >
              <span class="el-upload-list__item-actions">
        <span
            class="el-upload-list__item-preview"
            @click="handlePictureCardPreview(file)"
        >
          <i class="el-icon-zoom-in"></i>
        </span>
        <span
            v-if="!disabled"
            class="el-upload-list__item-delete"
            @click="handleDownload(file)"
        >
          <i class="el-icon-download"></i>
        </span>
        <span
            v-if="!disabled"
            class="el-upload-list__item-delete"
            @click="handleRemove(file)"
        >
          <i class="el-icon-delete"></i>
        </span>
      </span>
            </div>
          </el-upload>
          <el-dialog :visible.sync="dialogVisible">
            <img width="100%" height="100%" :src="dialogImageUrl" alt="">
          </el-dialog>
        </div>


      </div>
    </div>

    <div>

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
export default {
  data() {
    return {
      file: {},
      dropFiles: [],
      dialogImageUrl: '',
      dialogVisible: false,
      disabled: false,
      playerOptions: {
        playbackRates: [0.5, 1.0, 1.5, 2.0], // play speed
        autoplay: false,
        muted: false,     // default set as false
        loop: false,      // restart the video or not
        preload: 'auto',  // set to auto, check by the browser.
        language: 'zh-CN',
        aspectRatio: '16:9',  // "16:9" or "4:3"）
        fluid: true,  // 当true时，Video.js player  will self-adapt the window size
        sources: [{
          type: "video/mp4",  // type
          // url地址
          src: 'http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4' ,
        }],
        poster: '',
        notSupportedMessage: 'This video is not able to play',  // display when video is not able to play
        controlBar: {
          timeDivider: true,           // divider for current time and remaining time
          durationDisplay: true,       // duration timw
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
        fluid: true,  // 当true时，Video.js player  will self-adapt the window size
        sources: [{
          type: "video/mp4",  // type
          // url
          src: "https://media.w3.org/2010/05/sintel/trailer.mp4"
        }],
        poster: '',
        notSupportedMessage: 'This video is not able to play',  // display when video is not able to play
        controlBar: {
          timeDivider: true,           // divider for current time and remaining time
          durationDisplay: true,       // duration timw
          remainingTimeDisplay: false, // display the remaining time or not
          fullscreenToggle: true       // full screen button
        },

      }


    }
  },
  methods: {
    deleteDropFile(index) {
      this.dropFiles.splice(index, 1)
    },
    handleRemove(file) {
      console.log(file);
      let fileList = this.$refs.upload.uploadFiles;
      let index = fileList.findIndex( fileItem => {return fileItem.uid === file.uid});
      fileList.splice(index, 1);
    },
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },
    handleDownload(file) {
      console.log(file);
    }
  }

}

</script>
