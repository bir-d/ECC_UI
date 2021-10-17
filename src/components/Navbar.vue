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
            <b-navbar-item tag="div">
                <div class="buttons">
                    <a class="button is-large" @click="modalActive = true">
                        <p id="button-text">+ Preset</p>
                    </a>
                    <!-- PRESET MODAL / DIALOG HTML STARTS HERE -->
                    <b-modal v-model="modalActive">
                        <header class="modal-card-head">
                            <p class="modal-card-title">Save Preset</p>
                            <button
                              type="button"
                              class="delete"
                              @click="$emit('close')"/>
                        </header>

                        <section class="modal-card-body">
                        <b-field label="Preset name">
                            <b-input
                                type="text"
                                :value="preset_name"
                                placeholder="Preset name"
                                required>
                            </b-input>
                        </b-field>
                        </section>

                        <footer class="modal-card-foot">
                        <b-button
                            label="Close"
                            @click="$emit('close')" />
                        <b-button
                            label="Save"
                            type="is-primary" />
                    </footer>

                    </b-modal>
                    <!-- PRESET MODAL / DIALOG HTML ENDS HERE -->
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
</style>

<script>
import axios from 'axios'




export default ({
    name: 'App',
    data() {
        return {
        presetnum: 5,
        test:[],
        modalActive: false
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
