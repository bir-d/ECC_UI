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
