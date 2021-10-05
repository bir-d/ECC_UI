<template>
    <div>
        <div class="columns">
            <div class="column is-half">
                <div class="video-wall">
                    <div class="upload">
                        <input type="file" @change="onFileChange">
                    </div>
                    <div class="video-player">
                        <video controls>
                            <source type="video/mp4" v-for="(videos,index) in dropFiles" :key="index" class="tag is-primary" src=videos.address />
                        </video>
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
export default {
  data() {
    return {
      file: {},
      dropFiles: [
          {
              label: String,
              address: String
          }
      ]
    };
  },
  methods: {
    deleteDropFile(index) {
      this.dropFiles.splice(index, 1);
    },
    onFileChange(video) {
        var files = video.target.files || video.dataTransfer.files;
        if(!files.length){
            return;
        }
        this.createImage(files[0])
    },
    createVideo(file) {
        var reader = new FileReader();
        var vm = this;
        reader.onload = (video) => {
            vm.image = video.target.result;
        };
        reader.readAsDataURL(file);
    }
  }
};
</script>
