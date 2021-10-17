<template>
  <div class="overall">
    <div class="columns">
      <div class="column">
        <!--  Video wall section -->
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
        <!--  Workstations section -->
        <a href="/workstation">
          <figure class="image is-16by9">
            <img src="../assets/home-workstation.png">
          </figure>
          <div class="content" id="title-label">
            <h4>Workstations</h4>
          </div>
        </a>
      </div>
      <div class="column">
        <!--  Lights section -->
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
        <!--  Displays section -->
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
        <!--  Container storing the recently used presets -->
        <h2 class="is-size-3 is-underlined has-text-left">Recently Used</h2>
      </div>
      <!-- aniamtion for presets -->
      <sequential-entrance>
      <div class="columns" id="recent-section">
        <!-- Lists out presets in db in list -->
        <div class="column is-2" v-for="element in test.slice(0,5)" :key="element">
            <div class="level-item has-text-centered">
              <a>
                <figure class="image is-128x128">
                  <img id="recent-image" class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png" v-on:click="getPreset(element.preset_name)">
                </figure>
                
                <div class="content has-text-centered is-size-5" id="title-label">
                  <p> {{ element.preset_name }}</p>
                </div>
              </a>
            </div>
        </div>
        <div class="column is-2">
            <div class="level-item has-text-centered">
              <a href="/presets">
                <figure class="image is-128x128">
                  <img id="recent-image" class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png" v-on:click="getPreset(element.preset_name)">
                </figure>
                
                <div class="content has-text-centered is-size-5" id="title-label">
                  <p> View More</p>
                </div>
              </a>
            </div>
        </div>
        </div>
        </sequential-entrance>
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
      // Create lists for database data to enter
      dblights: [],
      dbvideo: [],
      dbworkstations: [],
      dbdisplays: [],
      test: [],
      presetnum: 0,
    }

  },
  created() {
            // Extracts ECC information stored in database
            this.getLights();
            this.getVideoWall();
            this.getWorkStations();
            this.getDisplays();
            this.getPreset("");
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
      }).then((response) => {

          this.isLoaded = true;

          // Check the response was a success
          if(response.data != 'undefined')
          {
              this.dblights = response.data;
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
      
      }).then((response) => {

          this.isLoaded = true;

          // Check the response was a success
          if(response.data != 'undefined')
          {
              this.dbvideo = response.data;
              
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
      
      }).then((response) => {

          this.isLoaded = true;

          // Check the response was a success
          if(response.data != 'undefined')
          {
              this.dbworkstations = response.data;
              
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
      
      }).then((response) => {

          this.isLoaded = true;

          // Check the response was a success
          if(response.data != 'undefined')
          {
              this.dbdisplays = response.data;
              
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
      
      }).then((response) => {

          this.isLoaded = true;

          // Check the response was a success
          if(response.data != 'undefined')
          {
              this.presetnum = response.data.length
              if (PresetName != ""){
                for(let i = 0; i < response.data.length; i++){
                  if(PresetName == response.data[i].preset_name) {
                    var temp = response.data[i]
                    this.UpdateDB(temp)
                  }
              }
              }
              
              this.test = response.data;
              
          }
      });
    },
    //Update database when a preset is called
    UpdateDB(data) {
      for(let i = 0; i < data.lights.length; i++){
        axios({
          method:'put',
          url: 'http://127.0.0.1:8000/api/lights/' + data.lights[i].id,
          headers: {
            'Content-Type': 'application/json'
          },
          data: {
            brightness: data.lights[i].brightness, 
            colour: data.lights[i].colour,
            id: data.lights[i].id,
            light_on: data.lights[i].light_on,
            name: data.lights[i].name,
            selected: data.lights[i].selected,
          },
          auth: {
            username: 'admin',
            password: 'eccadmin123'
          }
        })
      }
      for(let i = 0; i < data.video_Wall.length; i++){
        axios({
          method:'put',
          url: 'http://127.0.0.1:8000/api/video_wall/' + data.video_Wall[i].id,
          headers: {
            'Content-Type': 'application/json'
          },
          data: {
            id: data.video_Wall[i].id,
            source: data.video_Wall[i].source,
            media_name: data.video_Wall[i].media_name,
            media_type: data.video_Wall[i].media_type,
            wall_on: data.video_Wall[i].wall_on,
          },
          auth: {
            username: 'admin',
            password: 'eccadmin123'
          }
        })
      }
      console.log(data.displays)
      for(let i = 0; i < data.displays.length; i++){
        axios({
          method:'put',
          url: 'http://127.0.0.1:8000/api/displays/' + data.displays[i].id,
          headers: {
            'Content-Type': 'application/json'
          },
          data: {
            id: data.displays[i].id,
            display_name: data.displays[i].display_name,
            display_on: data.displays[i].display_on,
            media_name: data.displays[i].media_name,
            media_type: data.displays[i].media_type,
            source: data.displays[i].source,
          },
          auth: {
            username: 'admin',
            password: 'eccadmin123'
          }
        })
      }
      for(let i = 0; i < data.workstations.length; i++){
        axios({
          method:'put',
          url: 'http://127.0.0.1:8000/api/workstations/' + data.workstations[i].id,
          headers: {
            'Content-Type': 'application/json'
          },
          data: {
            id: data.workstations[i].id,
            source: data.workstations[i].source,
            media_name: data.workstations[i].media_name,
            media_type: data.workstations[i].media_type,
            station_on: data.workstations[i].station_on,
            workstation_name: data.workstations[i].workstation_name,
          },
          auth: {
            username: 'admin',
            password: 'eccadmin123'
          }
        })
      }
      
    },
    pushPreset(PresetName) {
    axios({
        method:'post',
        url: 'http://127.0.0.1:8000/api/preset/',
        data: { // Send description and status to the server
            id: this.presetnum + 1,
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
        let newPreset = {'id': response.data.id, 'preset_name': PresetName, 'lights': this.dblights, 'video_Wall': this.dbvideo, 'workstations': this.dbworkstations, 'displays': this.dbdisplays}
        this.presetnum = this.presetnum + 1
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
