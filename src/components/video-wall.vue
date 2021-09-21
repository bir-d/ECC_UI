<template>
    <div>
        <div class="columns">
            <div class="column is-half">
                <b-field class="video-wall">
                    <b-upload v-model="dropFiles" multiple drag-drop expanded class="wall-piece">
                        <section class="section">
                        <div class="content has-text-centered">
                            <p>Drop your files here</p>
                        </div>
                        </section>
                    </b-upload>
                    <b-upload v-model="dropFiles" multiple drag-drop expanded class="wall-piece">
                        <section class="section">
                        <div class="content has-text-centered">
                            <p>Drop your files here</p>
                        </div>
                        </section>
                    </b-upload>
                    <b-upload v-model="dropFiles" multiple drag-drop expanded class="wall-piece">
                        <section class="section">
                        <div class="content has-text-centered">
                            <p>Drop your files here</p>
                        </div>
                        </section>
                    </b-upload>
                </b-field>
                <b-field class="video-wall">
                    <b-upload v-model="dropFiles" multiple drag-drop expanded class="wall-piece">
                        <section class="section">
                        <div class="content has-text-centered">
                            <p>Drop your files here</p>
                        </div>
                        </section>
                    </b-upload>
                    <b-upload v-model="dropFiles" multiple drag-drop expanded class="wall-piece">
                        <section class="section">
                        <div class="content has-text-centered">
                            <p>Drop your files here</p>
                        </div>
                        </section>
                    </b-upload>
                    <b-upload v-model="dropFiles" multiple drag-drop expanded class="wall-piece">
                        <section class="section">
                        <div class="content has-text-centered">
                            <p>Drop your files here</p>
                        </div>
                        </section>
                    </b-upload>
                </b-field>
                <b-field class="video-wall">
                    <b-upload v-model="dropFiles" multiple drag-drop expanded class="wall-piece">
                        <section class="section">
                        <div class="content has-text-centered">
                            <p>Drop your files here</p>
                        </div>
                        </section>
                    </b-upload>
                    <b-upload v-model="dropFiles" multiple drag-drop expanded class="wall-piece">
                        <section class="section">
                        <div class="content has-text-centered">
                            <p>Drop your files here</p>
                        </div>
                        </section>
                    </b-upload>
                    <b-upload v-model="dropFiles" multiple drag-drop expanded class="wall-piece">
                        <section class="section">
                        <div class="content has-text-centered">
                            <p>Drop your files here</p>
                        </div>
                        </section>
                    </b-upload>
                </b-field>
                <div class="tags">
                    <span v-for="(file, index) in dropFiles" :key="index" class="tag is-primary">
                        {{file.name}}
                        <button class="delete is-small" type="button" @click="deleteDropFile(index)"></button>
                    </span>
                </div>
            </div>
            <div class="column is-narrow">
                <section class="media-wall files">
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
.video-wall{
    margin-top: 3em;
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
    border-style: dashed;
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
      dropFiles: []
    };
  },
  methods: {
    deleteDropFile(index) {
      this.dropFiles.splice(index, 1);
    }
  }
};
</script>
