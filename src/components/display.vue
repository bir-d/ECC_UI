<template>
  <div class="content">
    <div class = 'left'>
      <section>

        <h1>Screen 1</h1>
        <b-carousel :indicator-inside="false">
          <b-carousel-item v-for="(item, i) in 6" :key="i">
            <b-image class="image" :src="getImgUrl1(i)"></b-image>
          </b-carousel-item>
          <template #indicators="props">
            <b-image class="al image" :src="getImgUrl1(props.i)" :title="props.i"></b-image>
          </template>
        </b-carousel>
        <h1>Screen2</h1>
        <video width=92% height="200px" controls  alt="screen2">
          <source src="https://www.youtube.com/watch?v=Oi1BcouEmio"  type="video/mp4" class = 'grid1'>
        </video>
        <div class = 'frame'>
          <b-field>
            <b-upload v-model="dropFiles" multiple drag-drop expanded class ='uploadWindow2'>
              <section class="section">
                <p>Drop your files here or click to upload</p>
              </section>
            </b-upload>
          </b-field>
          <div class="tags">
                    <span v-for="(file, index) in dropFiles" :key="index" class="tag is-primary" >
                        {{file.name}}
                        <button class="delete is-small" type="button" @click="deleteDropFile(index)">
                        </button>
                    </span>
          </div>
        </div>

      </section>
    </div>

    <div class = 'right'>
      <div>
        <h3 class = screen1>the images/videos for screen1</h3>
        <div class="imgBlock">
          <img src="https://picsum.photos/id/431/1230/500"  alt="grid1"
               draggable="true"
               class='grid1'>
          <img src="https://picsum.photos/id/432/1230/500"  class='grid1'>
          <img src="https://picsum.photos/id/433/1230/500"  class='grid1'>
        </div>
        <div class="imgBlock">
          <img src="https://picsum.photos/id/434/1230/500"  class='grid1'>
          <img src="https://picsum.photos/id/435/1230/500"  class='grid1'>
          <img src="https://picsum.photos/id/436/1230/500"  class='grid1'>
        </div>
      </div>

      <div >
        <h3 class="screen2">the images/videos for screen2</h3>
        <div class="imgBlock">
          <img src='../views/rectangle.png' alt="grid1" class='grid2'>
          <img src='../views/rectangle.png' alt="grid1" class='grid2'>
          <img src='../views/rectangle.png' alt="grid1" class='grid2'>
        </div>
        <div class="imgBlock">
          <img src='../views/rectangle.png' alt="grid1" class='grid2'>
          <img src='../views/rectangle.png' alt="grid1" class='grid2'>
          <img src='../views/rectangle.png' alt="grid1" class='grid2'>
        </div>
      </div>
    </div>
  </div>

</template>



<style scoped>
.is-active .al img {
  filter: grayscale(0%);
}
.al img {
  filter: grayscale(100%);
}
.frame{
  height:133px;
  max-width: 100%;
  border: 2px solid darkred;
  border-radius: 5px ;
  text-align-all: center;
  /*left:20px*/
}
.screen1{
  border-top: 2px solid darkred;
}
.screen2{
  margin-top: 200px;
  /*height: 300px;*/
  border-top: 2px solid darkred;
  /*border-radius: 5px ;*/
}
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
.grid1{
  margin:30px 35px;
}
.grid2{
  margin:30px 35px;
  filter: grayscale(100%);
  filter: grayscale(0%);
}
.imgBlock{
  width:100px;
  height: 150px;
  /*margin:0 50px;*/
  display:flex;
  flex-direction: row;
}
</style>


<script>
export default {
  data() {
    return {
      file:{},
      dropFiles: []
    }
  },
  methods: {
    getImgUrl1(value) {
      return `https://picsum.photos/id/43${value}/1230/500`
    },
    methods: {
      deleteDropFile(index) {
        this.dropFiles.splice(index, 1)
      }
    }
  }
}
</script>