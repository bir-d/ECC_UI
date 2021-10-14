<template>
  <div>
    <b-navbar>
        <template #brand>
            <b-navbar-brand tag="router-link" :to="{ path: '/' }" id="brand">
            <figure class="image is-128x128">
                <a href="/"><img src="../assets/navbar-thales-logo.png" alt="Thales Logo"></a>
            </figure>
            </b-navbar-brand>
        </template>
        <template #end>
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
    color: #6b705c;
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
</style>

<script>
import axios from 'axios'




export default ({
    name: 'App',
    data() {
        return {
        presetnum: 5,
        }
    },
    methods: {
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
                let newPreset = {'id': response.data.id, 'preset_name': this.preset_name, 'lights': this.lights, 'video_Wall': this.video_Wall, 'workstations': this.workstations, 'displays': this.displays}
                this.presetnum = this.presetnum + 1
                this.test.push(newPreset)
                })
                .catch((error) => {
                console.log(error.response);
                console.log(error.request);
                console.log(error.message);
                });
    }
    }
})
</script>
