<template>
  <div class="overall">
    <hr>
    <div class="recents">
      <div class="columns" id="recent-section" v-for="ranger in presetrange" :key="ranger">
        <!-- Lists out presets in db in list -->

        <div class="column is-2" v-for="element in presets.slice(ranger[0],ranger[1])" :key="element">
            <div class="level-item has-text-centered">
              <a>
                <figure class="image is-128x128">
                  <img id="recent-image" class="is-large is-rounded"  src="https://bulma.io/images/placeholders/480x480.png" v-on:click="getPreset(element.preset_name)">
                </figure>
                
                <div class="content has-text-centered is-size-5" id="title-label">
                  <p> {{ element.preset_name }}</p>
                </div>
              </a>
            </div>
        </div>
        <br>
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
      // create lists for db data to enter
      presets: [],
      presetnum: 0,
      presetrange: [],
    }

  },
  created() {
            // Extracts ECC information stored in db
            this.getPresets();
            //this.PresetIndex();
        },
  methods: {
    getPresets() {
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
              
            this.presets = response.data;
            this.presetnum = response.data.length
            for(let i = 0; i < this.presetnum; i+=5){
                this.presetrange.push([i,i+5])
            }
              
          }
      });
    },

  },
})
</script>
