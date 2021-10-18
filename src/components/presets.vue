<template>
  <div class="overall">
    <h1 class="title is-1"> Presets </h1>
    <hr>
    <div class="recents">
      <sequential-entrance>
      <div class="columns" id="recent-section" v-for="ranger in presetrange" :key="ranger">
        <!-- Lists out presets in db in list -->

        <div class="column is-2" v-for="element in presets.slice(ranger[0],ranger[1])" :key="element">
            <div class="level-item has-text-centered">
              <a>
                <figure class="image is-128x128">
                  <img id="recent-image" class="is-large is-rounded"  src="https://bulma.io/images/placeholders/480x480.png" v-on:click="getPreset(element.preset_name, true)">
                </figure>
                
                <div class="content has-text-centered is-size-5" id="title-label">
                  <p> {{ element.preset_name }}</p>
                </div>
              </a>
            </div>
        </div>
        <br>
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
      // create lists for db data to enter
      presets: [],
      presetnum: 0,
      presetrange: [],
      test: [],
    }

  },
  created() {
            // Extracts ECC information stored in db
            this.getPreset("");
            //this.PresetIndex();
        },
  methods: {
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
    getPreset(PresetName, launchNotification = false) {
        console.log(PresetName)
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
              console.log()
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

      // only if notification specified
      if (launchNotification){
          this.$buefy.notification.open({
              message: 'Preset "' + PresetName +'" was successfully loaded!',
              duration: 5000,
              position: "is-bottom-right",
              type: 'is-success',
              hasIcon: true,
              queue: false
          })
      }
    },
  },
})
</script>
