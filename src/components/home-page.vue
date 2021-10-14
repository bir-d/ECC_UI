<template>
  <div class="overall">
    <div class="columns">
      <div class="column">
        <a href="/videowall">
          <figure class="image is-16by9">
            <img src="../assets/home-video-wall.png">
          </figure>
          <div class="content" id="title-label">
            <h4>Video Wall</h4>
          </div>
        </a>
      </div>
      <div class="column">
        <a href="#">
          <figure class="image is-16by9">
            <img src="../assets/home-workstation.png">
          </figure>
          <div class="content" id="title-label">
            <h4>Workstations</h4>
          </div>
        </a>
      </div>
      <div class="column">
        <a href="/lights">
          <figure class="image is-16by9">
            <img src="../assets/home-lights.png">
          </figure>
          <div class="content" id="title-label">
            <h4>Lights</h4>
          </div>
        </a>
      </div>
      <div class="column">
        <a href="/display">
          <figure class="image is-16by9">
            <img src="../assets/home-displays.png">
          </figure>
          <div class="content" id="title-label">
            <h4>Displays</h4>
          </div>
        </a>
      </div>
    </div>
    <hr>
    <div class="recents">
      <div class="content">
        <h2 class="is-size-3 is-underlined has-text-left">Recently Used</h2>
      </div>
      <div class="columns" id="recent-section">
        <div class="column is-2">
            <div class="level-item has-text-centered">
              <a>
                <figure class="image is-128x128">
                  <img id="recent-image" class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
                </figure>
                <div class="content has-text-centered is-size-5" id="title-label">
                  <p>Preset</p>
                </div>
              </a>
            </div>
          </div>
          <div class="column is-2">
            <div class="level-item has-text-centered">
              <a>
                <figure class="image is-128x128">
                  <img id="recent-image" class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
                </figure>
                <div class="content has-text-centered is-size-5" id="title-label">
                  <p>Preset</p>
                </div>
              </a>
            </div>
          </div>
          <div class="column is-2">
            <div class="level-item has-text-centered">
              <a>
                <figure class="image is-128x128">
                  <img id="recent-image" class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
                </figure>
                <div class="content has-text-centered is-size-5" id="title-label">
                  <p>Preset</p>
                </div>
              </a>
            </div>
          </div>
          <div class="column is-2">
           <div class="level-item has-text-centered">
              <a>
                <figure class="image is-128x128">
                  <img id="recent-image" class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
                </figure>
                <div class="content has-text-centered is-size-5" id="title-label">
                  <p>Preset</p>
                </div>
              </a>
            </div>
          </div>
          <div class="column is-2">
            <div class="level-item has-text-centered">
              <a>
                <figure class="image is-128x128">
                  <img id="recent-image" class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
                </figure>
                <div class="content has-text-centered is-size-5" id="title-label">
                  <p>Preset</p>
                </div>
              </a>
            </div>
          </div>
          <div class="column is-2">
            <div class="level-item has-text-centered">
              <a>
                <figure class="image is-128x128">
                  <img id="recent-image" class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
                </figure>
                <div class="content has-text-centered is-size-5" id="title-label">
                  <p>Preset</p>
                </div>
              </a>
            </div>
          </div>
        </div>
    </div>
  </div>
</template>

<style scoped>
.overall{
  margin-top: 6em;
  margin-bottom: 4em;
  margin-left: 3em;
  margin-right: 3em;
}
#recent-section{
  margin-left: 2em;
  margin-top: 2em;
}
#title-label{
  margin-top: 2em;
  font-family: monospace;
}
figure{
  transition: all 0.2s ease;
  transition-property: transform, opacity, color, border-color, background-color;
}
figure:hover{
  transform: scale(1.05);
}
</style>

<script>
  import axios from 'axios'

export default ({
  name: 'App',
  data() {
    return {
      dblights: [],
      dbvideo: [],
      dbworkstations: [],
      dbdisplays: [],
      test: [],
    }

  },
  created() {
            // Extracts light information stored in db
            this.getLights();
            this.getVideoWall();
            this.getWorkStations();
            this.getDisplays();
            this.getPreset("Test2");
        },
  methods: {
    getLights() {
      axios({
          method:'get',
          // Url of backend location of data
          url: 'http://127.0.0.1:8000/api/lights/',
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
              this.dblights = response.data;
              // Calls function to update lights values with db values
              //this.updateLights();
          }
      });
    },
    getVideoWall() {
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
              this.dbvideo = response.data;
              // Calls function to update lights values with db values
              //this.updateLights();
          }
      });
    },
    getWorkStations() {
      axios({
          method:'get',
          // Url of backend location of data
          url: 'http://127.0.0.1:8000/api/workstations/',
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
              this.dbworkstations = response.data;
              // Calls function to update lights values with db values
              //this.updateLights();
          }
      });
    },
    getDisplays() {
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

          this.isLoaded = true;

          // Check the response was a success
          if(response.data != 'undefined')
          {
              this.dbdisplays = response.data;
              // Calls function to update lights values with db values
              //this.updateLights();
          }
      });
    },
    getPreset(PresetName) {
      axios({
          method:'get',
          // Url of backend location of data
          url: 'http://127.0.0.1:8000/api/preset/',
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
              var presetindex = NaN
              for(let i = 0; i < response.data.length; i++){
                if(PresetName == response.data[i].preset_name) {
                  console.log(response.data[i].preset_name)
                  presetindex = i
                }
              }
              console.log(presetindex)
              this.test = response.data;
              // Calls function to update lights values with db values
              //this.updateLights();
          }
      });
    },
    pushPreset(PresetName) {
      console.log(this.dblights)
      axios({
          method:'post',
          url: 'http://127.0.0.1:8000/api/preset/',
          data: { // Send description and status to the server
            id: "3",
            preset_name: PresetName,
            lights: this.dblights,
            video_Wall: this.dbvideo,
            workstations: this.dbworkstations,
            displays: this.dbdisplays,
          },
          auth: { // Basic authentication
            username: 'admin',
            password: 'eccadmin123'
          }
        }).then((response) => {
          let newPreset = {'id': response.data.id, 'preset_name': this.preset_name, 'lights': this.lights, 'video_Wall': this.video_Wall, 'workstations': this.workstations, 'displays': this.displays}

          this.test.push(newPreset)
        })
        .catch((error) => {
          console.log(error.response);
          console.log(error.request);
          console.log(error.message);
        });
    }

  },
})
</script>
