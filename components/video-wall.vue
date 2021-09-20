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
                <section class="media-wall">
                    <div class="columns">
                        <div class="column">
                            <img src="https://bulma.io/images/placeholders/128x128.png">
                        </div>
                        <div class="column">
                            <img src="https://bulma.io/images/placeholders/128x128.png">
                        </div>
                        <div class="column">
                            <img src="https://bulma.io/images/placeholders/128x128.png">
                        </div>
                        <div class="column">
                            <img src="https://bulma.io/images/placeholders/128x128.png">
                        </div>
                    </div>
                    <div class="columns">
                        <div class="column">
                            <img src="https://bulma.io/images/placeholders/128x128.png">
                        </div>
                        <div class="column">
                            <img src="https://bulma.io/images/placeholders/128x128.png">
                        </div>
                        <div class="column">
                            <img src="https://bulma.io/images/placeholders/128x128.png">
                        </div>
                        <div class="column">
                            <img src="https://bulma.io/images/placeholders/128x128.png">
                        </div>
                    </div>
                    <div class="columns">
                        <div class="column">
                            <img src="https://bulma.io/images/placeholders/128x128.png">
                        </div>
                        <div class="column">
                            <img src="https://bulma.io/images/placeholders/128x128.png">
                        </div>
                        <div class="column">
                            <img src="https://bulma.io/images/placeholders/128x128.png">
                        </div>
                        <div class="column">
                            <img src="https://bulma.io/images/placeholders/128x128.png">
                        </div>
                    </div>
                    <div class="columns">
                        <div class="column">
                            <img src="https://bulma.io/images/placeholders/128x128.png">
                        </div>
                        <div class="column">
                            <img src="https://bulma.io/images/placeholders/128x128.png">
                        </div>
                        <div class="column">
                            <img src="https://bulma.io/images/placeholders/128x128.png">
                        </div>
                        <div class="column">
                            <img src="https://bulma.io/images/placeholders/128x128.png">
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
</style>

<script>
export default {
  data() {
    return {
      file: {},
      dropFiles: []
    }
  },
  methods: {
    deleteDropFile(index) {
      this.dropFiles.splice(index, 1);
    }
  }
};
</script>
