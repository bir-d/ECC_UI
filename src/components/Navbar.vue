<template>
  <div>
    <b-navbar style="min-height:128px;">
        <template #brand>
            <b-navbar-brand v-if="$route.name==='home'" tag="router-link" :to="{ path: '/' }" id="brand">
            <figure class="image is-128x128">
                <a href="/"><img src="../assets/navbar-thales-logo.png" alt="Thales Logo"></a>
            </figure>
            </b-navbar-brand>
            <b-navbar-item v-else tag="div">
                <a href="/">
                    <b-icon pack="fas" icon="arrow-left" size=is-large></b-icon>
                </a>
            </b-navbar-item>
        </template>
        <template #end>
            <b-navbar-button v-if="$route.name==='home'" tag="div" :to="{ path: '/' }">
                <a id="power-button">
                    <img src="../assets/power-button.png" v-on:click="power()"> 
                </a>   
            </b-navbar-button>
            <b-navbar-item tag="div">
                <div class="buttons">
                    <a class="button is-large">
                        <p id="button-text">+ Preset</p>
                    </a>
                </div>
            </b-navbar-item>
        </template>
    </b-navbar>
  </div>    
</template>

<style scoped>
a {
  color: #42b983;
}
#navbar{
    font-size: 15px;
    font-family: monospace;
    color: #0a0a09;
}
#button-text{
    font-family: monospace;
    color: white;
}
.button{
    background-color:#6b705c;
}
#brand{
    margin-left: 25px;
    margin-right: 25px;
}
#power-button img {
    width: 75px;
    height: 75px;
    margin-top: 25px;
    margin-right: 25px;
}
#power-button img:active {
    transform: scale(0.95);
    transition: all 0.2s ease;
}
</style>

<script>
import axios from 'axios'




export default ({
    name: 'App',
    data() {
        return {
        
        presetnum: 5,
        test:[],
        }
        
    },
   
    created() {
            // Extracts ECC information stored in database
            this.getPreset("");
    },

    methods: {

        // Change power state of room
        power() {
        
            // Check if currently on and load in off preset
            if (localStorage.getItem("state") == 'on'){
                this.getPreset('Off')
                localStorage.setItem("state", 'off');
            }
            
            // Otherwise load in defualt preset
            else {
                this.getPreset('Default')
                localStorage.setItem("state", 'on');

            }

        },
        pushPreset(PresetName) {
            axios({
                method:'post',
                url: 'http://127.0.0.1:8000/api/preset/',
                data: { // Send description and status to the server
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
                this.presetnum = this.presetnum + 1
                this.test.push(newPreset)
                })
                .catch((error) => {
                console.log(error.response);
                console.log(error.request);
                console.log(error.message);
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
      
    }
    }
})
</script>
